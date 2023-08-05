import logging
from html import escape

from django.apps import apps
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.http import Http404
from django.template.defaultfilters import floatformat
from django.urls import reverse
from django.utils import timezone as django_timezone
from django.utils.functional import cached_property, keep_lazy_text
from django.utils.safestring import mark_safe
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.utils.translation import override

from ....matomo_api.matomo_api_client import MatomoApiClient
from ....nominatim_api.utils import BoundingBox
from ...constants import (
    administrative_division,
    machine_translation_permissions,
    months,
    region_status,
)
from ...utils.translation_utils import gettext_many_lazy as __
from ..abstract_base_model import AbstractBaseModel
from ..offers.offer_template import OfferTemplate

logger = logging.getLogger(__name__)


@keep_lazy_text
def format_deepl_help_text(help_text):
    """
    Helper function to lazily format help text with number separators

    :param help_text: DeepL field help text to format
    :type help_text: django.utils.functional.Promise

    :return: formatted help text
    :rtype: django.utils.functional.Promise
    """
    return help_text.format(
        floatformat(settings.DEEPL_CREDITS_ADDON, "g"),
        floatformat(settings.DEEPL_CREDITS_FREE, "g"),
    )


# pylint: disable=too-few-public-methods
class RegionManager(models.Manager):
    """
    This manager annotates each region object with its language tree root node.
    This is done because it is required to calculate the region's
    :attr:`~integreat_cms.cms.models.regions.region.Region.default_language` which is called in
    :attr:`~integreat_cms.cms.models.regions.region.Region.full_name`.
    """

    def get_queryset(self):
        """
        Get the queryset of regions including the custom attribute ``language_tree_root`` which contains the root node
        of the region's language tree.

        :return: The queryset of regions
        :rtype: ~django.db.models.query.QuerySet [ ~integreat_cms.cms.models.regions.region.Region ]
        """
        # Get model instead of importing it to avoid circular imports
        LanguageTreeNode = apps.get_model(
            app_label="cms", model_name="LanguageTreeNode"
        )
        return (
            super()
            .get_queryset()
            .prefetch_related(
                models.Prefetch(
                    "language_tree_nodes",
                    queryset=LanguageTreeNode.objects.all().select_related("language"),
                    to_attr="prefetched_language_tree_nodes",
                )
            )
        )


# pylint: disable=too-many-public-methods
class Region(AbstractBaseModel):
    """
    Data model representing region.
    """

    name = models.CharField(max_length=200, verbose_name=_("name"))
    #: See `community identification number <https://en.wikipedia.org/wiki/Community_Identification_Number>`__
    #: and `Gemeindeschlüssel (German) <https://de.wikipedia.org/wiki/Amtlicher_Gemeindeschl%C3%BCssel>`__
    common_id = models.CharField(
        max_length=48,
        blank=True,
        verbose_name=_("community identification number"),
        help_text=_(
            "Number sequence for identifying politically independent administrative units"
        ),
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        allow_unicode=True,
        verbose_name=_("URL parameter"),
        help_text=__(
            _("Unique string identifier without spaces and special characters."),
            _("Leave blank to generate unique parameter from name"),
        ),
    )
    #: Manage choices in :mod:`~integreat_cms.cms.constants.region_status`
    status = models.CharField(
        max_length=8,
        choices=region_status.CHOICES,
        default=region_status.HIDDEN,
        verbose_name=_("status"),
    )

    #: Manage choices in :mod:`~integreat_cms.cms.constants.administrative_division`.
    #: Also see `administrative division <https://en.wikipedia.org/wiki/Administrative_division>`__.
    administrative_division = models.CharField(
        max_length=24,
        choices=administrative_division.CHOICES,
        default=administrative_division.RURAL_DISTRICT,
        verbose_name=_("administrative division"),
    )
    aliases = models.JSONField(
        default=dict,
        blank=True,
        verbose_name=_("aliases"),
        help_text=__(
            _("E.g. smaller municipalities in that area."),
            _("If empty, the CMS will try to fill this automatically."),
            _("Specify as JSON."),
        ),
    )
    custom_prefix = models.CharField(
        max_length=48,
        blank=True,
        verbose_name=_("custom prefix"),
        help_text=__(
            _("Enter parts of the name that should not affect sorting."),
            _(
                "Use this field only if the prefix is not an available choice in the list of administrative divisions above."
            ),
        ),
    )
    events_enabled = models.BooleanField(
        default=True,
        verbose_name=_("activate events"),
        help_text=_("Whether or not events are enabled in the region"),
    )
    locations_enabled = models.BooleanField(
        default=False,
        verbose_name=_("activate locations"),
        help_text=_("Whether or not locations are enabled in the region"),
    )
    push_notifications_enabled = models.BooleanField(
        default=True,
        verbose_name=_("activate push notifications"),
        help_text=_("Whether or not push notifications are enabled in the region"),
    )
    latitude = models.FloatField(
        null=True,
        verbose_name=_("latitude"),
        help_text=_("The latitude coordinate of an approximate center of the region"),
    )
    longitude = models.FloatField(
        null=True,
        verbose_name=_("longitude"),
        help_text=_("The longitude coordinate of an approximate center of the region"),
    )
    longitude_min = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("minimum longitude"),
        help_text=_("The left boundary of the region"),
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)],
    )
    latitude_min = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("minimum latitude"),
        help_text=_("The bottom boundary of the region"),
        validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)],
    )
    longitude_max = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("maximum longitude"),
        help_text=_("The right boundary of the region"),
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)],
    )
    latitude_max = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("maximum latitude"),
        help_text=_("The top boundary of the region"),
        validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)],
    )
    postal_code = models.CharField(
        max_length=10,
        verbose_name=_("postal code"),
        help_text=_(
            "For districts, enter the postcode of the administrative headquarters."
        ),
    )

    admin_mail = models.EmailField(
        verbose_name=_("email address of the administrator"),
    )

    timezone = models.CharField(
        max_length=150,
        default=settings.CURRENT_TIME_ZONE,
        verbose_name=_("timezone"),
    )
    created_date = models.DateTimeField(
        default=django_timezone.now,
        verbose_name=_("creation date"),
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_("modification date"),
    )

    statistics_enabled = models.BooleanField(
        default=False,
        verbose_name=_("activate statistics"),
        help_text=_("Whether or not statistics are enabled for the region"),
    )
    seo_enabled = models.BooleanField(
        default=False,
        verbose_name=_("activate SEO section"),
        help_text=_(
            "Enable possibility to fill meta description for pages, events and locations"
        ),
    )
    matomo_id = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name=_("Matomo ID"),
        help_text=__(
            _("The Matomo ID of this region."),
            _("Will be automatically derived from the Matomo access token."),
        ),
    )
    matomo_token = models.CharField(
        max_length=150,
        blank=True,
        default="",
        verbose_name=_("Matomo authentication token"),
        help_text=_(
            "The secret Matomo access token of the region is used to authenticate in API requests"
        ),
    )

    page_permissions_enabled = models.BooleanField(
        default=False,
        verbose_name=_("activate page-specific permissions"),
        help_text=_(
            "This allows individual users to be granted the right to edit or publish a specific page."
        ),
    )

    icon = models.ForeignKey(
        "cms.MediaFile",
        verbose_name=_("logo"),
        on_delete=models.SET_NULL,
        related_name="icon_regions",
        blank=True,
        null=True,
    )

    chat_enabled = models.BooleanField(
        default=True,
        verbose_name=_("activate author chat"),
        help_text=_(
            "This gives all users of this region access to the cross-regional author chat."
        ),
    )

    administrative_division_included = models.BooleanField(
        default=False,
        verbose_name=_("include administrative division into name"),
        help_text=__(
            _(
                "Determines whether the administrative division is displayed next to the region name."
            ),
            _(
                "Sorting is always based on the name, independently from the administrative division."
            ),
        ),
    )

    offers = models.ManyToManyField(
        OfferTemplate,
        related_name="regions",
        blank=True,
        verbose_name=_("offers"),
        help_text=__(
            _(
                "Integreat offers are extended features apart from pages and events and are usually offered by a third party."
            ),
            _(
                "In most cases, the url is an external API endpoint which the frontend apps can query and render the results inside the Integreat app."
            ),
        ),
    )

    short_urls_enabled = models.BooleanField(
        default=False,
        verbose_name=_("Activate short urls"),
        help_text=_("Please check the box if you want to use short urls."),
    )

    external_news_enabled = models.BooleanField(
        default=False,
        verbose_name=_("Enable external news"),
        help_text=_(
            "Enable to display external articles in addition to local news managed by the CMS"
        ),
    )

    fallback_translations_enabled = models.BooleanField(
        default=True,
        verbose_name=_("Show content in default language as fallback"),
        help_text=_(
            "Whether or not events and locations are shown in default language as fallback"
        ),
    )

    hix_enabled = models.BooleanField(
        default=False,
        verbose_name=_("Activate HIX analysis"),
        help_text=_(
            "Allow users of this region to analyze understandability of text content via TextLab API."
        ),
    )

    summ_ai_enabled = models.BooleanField(
        default=False,
        verbose_name=_("activate automatic translations via SUMM.AI"),
        help_text=_(
            "Whether automatic translations into Easy German with SUMM.AI are enabled"
        ),
    )

    deepl_renewal_month = models.PositiveIntegerField(
        choices=months.CHOICES,
        default=months.JANUARY,
        verbose_name=_("DeepL credits renewal date"),
        help_text=_("Budget usage will be reset on the 1st of the month"),
    )

    deepl_addon_booked = models.BooleanField(
        default=False,
        verbose_name=_("DeepL add-on package booked"),
        help_text=format_deepl_help_text(
            _(
                "This makes {} translation credits available to the region instead of the {} free ones."
            )
        ),
    )

    deepl_midyear_start_month = models.PositiveIntegerField(
        default=None,
        blank=True,
        null=True,
        choices=months.CHOICES,
        verbose_name=_("DeepL budget year start date"),
        help_text=_("Month from which the add-on package was booked"),
    )

    deepl_budget_used = models.PositiveIntegerField(
        default=0,
        verbose_name=_("used DeepL budget"),
    )

    machine_translate_pages = models.PositiveIntegerField(
        choices=machine_translation_permissions.CHOICES,
        default=machine_translation_permissions.EVERYONE,
        verbose_name=_("Pages"),
    )

    machine_translate_events = models.PositiveIntegerField(
        choices=machine_translation_permissions.CHOICES,
        default=machine_translation_permissions.EVERYONE,
        verbose_name=_("Events"),
    )

    machine_translate_pois = models.PositiveIntegerField(
        choices=machine_translation_permissions.CHOICES,
        default=machine_translation_permissions.EVERYONE,
        verbose_name=_("Locations"),
    )

    #: Custom model manager :class:`~integreat_cms.cms.models.regions.region.RegionManager` for region objects
    objects = RegionManager()

    @cached_property
    def has_bounding_box(self):
        """
        Whether the region has an individual bounding box

        :return: Whether all required coordinates for the bounding box are set
        :rtype: bool
        """
        return all(
            [
                self.longitude_min,
                self.latitude_min,
                self.longitude_max,
                self.latitude_max,
            ]
        )

    @cached_property
    def bounding_box(self):
        """
        The bounding box of the region

        :return: A bounding box object
        :rtype: ~integreat_cms.nominatim_api.utils.BoundingBox
        """
        if self.has_bounding_box:
            return BoundingBox(
                self.latitude_min,
                self.latitude_max,
                self.longitude_min,
                self.longitude_max,
            )
        return settings.DEFAULT_BOUNDING_BOX

    @cached_property
    def language_tree(self):
        """
        This property returns a QuerySet of all
        :class:`~integreat_cms.cms.models.languages.language_tree_node.LanguageTreeNode` objects of this region.

        :return: A QuerySet of all active language tree nodes of this region
        :rtype: ~django.db.models.query.QuerySet [ ~integreat_cms.cms.models.languages.language_tree_node.LanguageTreeNode ]
        """
        try:
            # Try to get the prefetched language tree
            return self.prefetched_language_tree_nodes
        except AttributeError:
            # If the tree was not prefetched, query it from the database
            # (this should only happen in rare edge cases)
            return list(self.language_tree_nodes.all().select_related("language"))

    @cached_property
    def language_node_by_id(self):
        """
        This property returns this region's language tree nodes indexed by ids

        :return: A mapping from language tree node ids to their language tree nodes in this region
        :rtype: dict
        """
        return {node.id: node for node in self.language_tree}

    @cached_property
    def language_node_by_slug(self):
        """
        This property returns this region's language tree nodes indexed by slugs

        :return: A mapping from language slugs to their language tree nodes in this region
        :rtype: dict
        """
        return {node.slug: node for node in self.language_tree}

    @cached_property
    def languages(self):
        """
        This property returns a list of all :class:`~integreat_cms.cms.models.languages.language.Language` objects
        which have a :class:`~integreat_cms.cms.models.languages.language_tree_node.LanguageTreeNode` which belongs to
        this region.

        :return: A list of all :class:`~integreat_cms.cms.models.languages.language.Language` instances of this region
        :rtype: list [ ~integreat_cms.cms.models.languages.language.Language ]
        """
        return [node.language for node in self.language_tree]

    def get_source_language(self, language_slug):
        """
        This property returns this region's source language of a given language object

        :param language_slug: The slug of the requested language
        :type language_slug: str

        :return: The source language of the given language in this region
        :rtype: dict
        """
        try:
            parent_id = self.language_node_by_slug.get(language_slug).parent_id
            return self.language_node_by_id.get(parent_id).language
        except AttributeError:
            return None

    @cached_property
    def active_languages(self):
        """
        This property returns a list of all :class:`~integreat_cms.cms.models.languages.language.Language` objects
        which have  an active :class:`~integreat_cms.cms.models.languages.language_tree_node.LanguageTreeNode` which
        belongs to this region.

        :return: A list of all active :class:`~integreat_cms.cms.models.languages.language.Language` instances of this region
        :rtype: list [ ~integreat_cms.cms.models.languages.language.Language ]
        """
        return [node.language for node in self.language_tree if node.active]

    @cached_property
    def visible_languages(self):
        """
        This property returns a list of all :class:`~integreat_cms.cms.models.languages.language.Language` objects
        which have an active & visible :class:`~integreat_cms.cms.models.languages.language_tree_node.LanguageTreeNode`
        which belongs to this region.

        :return: A list of all active & visible :class:`~integreat_cms.cms.models.languages.language.Language` instances of this region
        :rtype: list [ ~integreat_cms.cms.models.languages.language.Language ]
        """
        return [
            node.language for node in self.language_tree if node.active and node.visible
        ]

    @cached_property
    def language_tree_root(self):
        """
        This property returns a the root node of the region's language tree

        :return: The region's language root node
        :rtype: ~integreat_cms.cms.models.languages.language_tree_node.LanguageTreeNode
        """
        return next(iter(self.language_tree), None)

    @cached_property
    def default_language(self):
        """
        This property returns the language :class:`~integreat_cms.cms.models.languages.language.Language` which
        corresponds to the root :class:`~integreat_cms.cms.models.languages.language_tree_node.LanguageTreeNode` of this
        region.

        :return: The root :class:`~integreat_cms.cms.models.languages.language.Language` of a region
        :rtype: ~integreat_cms.cms.models.languages.language.Language
        """
        return self.language_tree_root.language if self.language_tree_root else None

    @cached_property
    def prefix(self):
        """
        This property returns the administrative division of a region if it's included in the name.
        If this region has no default language, this property returns an empty string

        :return: The prefix of the region
        :rtype: str
        """
        if self.custom_prefix:
            return self.custom_prefix
        if self.administrative_division_included and self.default_language:
            # Get administrative division in region's default language
            with override(self.default_language.slug):
                return str(self.get_administrative_division_display())
        return ""

    @cached_property
    def full_name(self):
        """
        This property returns the full name of a region including its administrative division

        :return: The full name of the region
        :rtype: str
        """
        return f"{self.prefix} {self.name}".strip()

    @cached_property
    def region_users(self):
        """
        This property returns a QuerySet of all :class:`~django.contrib.auth.models.User` objects which belong to this
        region and are neither superusers nor staff.

        :return: A QuerySet of all :class:`~django.contrib.auth.models.User` object instances of a region
        :rtype: ~django.db.models.query.QuerySet [ ~django.contrib.auth.models.User ]
        """
        return get_user_model().objects.filter(
            regions=self,
            is_superuser=False,
            is_staff=False,
        )

    @cached_property
    def statistics(self):
        """
        This property returns the MatomoApiClient of the current region.

        :return: The statistics manager
        :rtype: ~django.db.models.query.QuerySet [ ~django.contrib.auth.models.User ]
        """
        return MatomoApiClient(self)

    def get_language_or_404(self, language_slug, only_active=False, only_visible=False):
        """
        This class method returns the requested language of this region with optional filters ``active`` and ``visible``

        :param language_slug: The slug of the requested language
        :type language_slug: str

        :param only_active: Whether to return only active languages
        :type only_active: bool

        :param only_visible: Whether to return only visible languages
        :type only_visible: bool

        :raises ~django.http.Http404: When no language with the given slug exists for this region and this filters

        :return: The requested :class:`~integreat_cms.cms.models.languages.language.Language` of this region
        :rtype: ~integreat_cms.cms.models.languages.language.Language
        """
        try:
            node = self.language_node_by_slug[language_slug]
            if only_active and not node.active:
                raise KeyError(
                    f"Language {node.language} is not active in region {self}"
                )
            if only_visible and not node.visible:
                raise KeyError(
                    f"Language {node.language} is not visible in region {self}"
                )
            return node.language
        except KeyError as e:
            raise Http404("No language matches the given query.") from e

    @cached_property
    def archived_pages(self):
        """
        This property returns a QuerySet of all archived pages and their descendants of this region.

        Per default, the returned queryset has some limitations because of the usage of
        :meth:`~django.db.models.query.QuerySet.union`. To perform the extra effort of returning an unrestricted
        queryset, use :meth:`~integreat_cms.cms.models.regions.region.Region.get_pages` with the parameters ``archived`` and
        ``return_unrestricted_queryset`` set to ``True``.

        :return: A QuerySet of all archived pages of this region
        :rtype: ~treebeard.ns_tree.NS_NodeQuerySet [ ~integreat_cms.cms.models.pages.page.Page ]
        """
        # Queryset of explicitly archived pages
        explicitly_archived_pages = self.pages.filter(explicitly_archived=True)
        # Multiple order_by clauses are not allowed in sql queries, so to make combined queries with union() work,
        # we have to remove ordering from the input querysets and apply the default ordering to the resulting queryset.
        explicitly_archived_pages = explicitly_archived_pages.order_by()
        # List of QuerySets of descendants of archived pages
        implicitly_archived_pages = [
            page.get_descendants().order_by() for page in explicitly_archived_pages
        ]
        # Merge explicitly and implicitly archived pages
        archived_pages = explicitly_archived_pages.union(*implicitly_archived_pages)
        # Order the resulting :class:`~treebeard.ns_tree.NS_NodeQuerySet` to restore the tree-structure
        return archived_pages.order_by("tree_id", "lft")

    @cached_property
    def non_archived_pages(self):
        """
        This property returns a QuerySet of all non-archived pages of this region.
        A page is considered as "non-archived" if its ``explicitly_archived`` property is ``False`` and all the
        page's ancestors are not archived as well.

        Per default, the returned queryset has some limitations because of the usage of
        :meth:`~django.db.models.query.QuerySet.difference` (see :meth:`~django.db.models.query.QuerySet.union` for some
        restrictions). To perform the extra effort of returning an unrestricted queryset, use
        :meth:`~integreat_cms.cms.models.regions.region.Region.get_pages` with the parameter
        ``return_unrestricted_queryset`` set to ``True``.

        :return: A QuerySet of all non-archived pages of this region
        :rtype: ~treebeard.ns_tree.NS_NodeQuerySet [ ~integreat_cms.cms.models.pages.page.Page ]
        """
        # Multiple order_by clauses are not allowed in sql queries, so to make combined queries with difference() work,
        # we have to remove ordering from the input querysets and apply the default ordering to the resulting queryset.
        archived_pages = self.archived_pages.order_by()
        # Exclude archived pages from all pages
        non_archived_pages = self.pages.difference(archived_pages)
        # Order the resulting TreeQuerySet to restore the tree-structure
        return non_archived_pages.order_by("tree_id", "lft")

    def get_pages(
        self,
        archived=False,
        return_unrestricted_queryset=False,
        prefetch_translations=False,
        prefetch_public_translations=False,
        annotate_language_tree=False,
    ):
        """
        This method returns either all archived or all non-archived pages of this region.
        To retrieve all pages independently of their archived-state, use the reverse foreign key
        :attr:`~integreat_cms.cms.models.regions.region.Region.pages`.

        Per default, the returned queryset has some limitations because of the usage of
        :meth:`~django.db.models.query.QuerySet.difference` and :meth:`~django.db.models.query.QuerySet.union`.
        To perform the extra effort of returning an unrestricted queryset, set the parameter
        ``return_unrestricted_queryset`` to ``True``.

        :param archived: Whether or not only archived pages should be returned (default: ``False``)
        :type archived: bool

        :param return_unrestricted_queryset: Whether or not the result should be returned as unrestricted queryset.
                                             (default: ``False``)
        :type return_unrestricted_queryset: bool

        :param prefetch_translations: Whether the latest translations for each language should be prefetched
                                      (default: ``False``)
        :type prefetch_translations: bool

        :param prefetch_public_translations: Whether the latest public translations for each language should be prefetched
                                             (default: ``False``)
        :type prefetch_public_translations: bool

        :param annotate_language_tree: Whether the pages should be annotated with the region's language tree
                                       (default: ``False``)
        :type annotate_language_tree: bool

        :return: Either the archived or the non-archived pages of this region
        :rtype: ~treebeard.ns_tree.NS_NodeQuerySet [ ~integreat_cms.cms.models.pages.page.Page ]
        """
        pages = self.archived_pages if archived else self.non_archived_pages
        if (
            return_unrestricted_queryset
            or prefetch_translations
            or prefetch_public_translations
        ):
            # Generate a new unrestricted queryset containing the same pages
            page_ids = [page.id for page in pages]
            pages = self.pages.filter(id__in=page_ids)
        if prefetch_translations:
            pages = pages.prefetch_translations()
        if prefetch_public_translations:
            pages = pages.prefetch_public_translations()
        if annotate_language_tree:
            pages = pages.annotate(language_tree=models.Subquery(self.language_tree))
        return pages

    def get_root_pages(self):
        """
        This method returns all root pages of this region.

        :return: This region's root pages
        :rtype: ~treebeard.ns_tree.NS_NodeQuerySet [ ~integreat_cms.cms.models.pages.page.Page ]
        """
        # Get model instead of importing it to avoid circular imports
        Page = apps.get_model(app_label="cms", model_name="Page")
        return Page.get_root_pages(region_slug=self.slug)

    @classmethod
    def search(cls, query):
        """
        Searches for all regions which match the given `query` in their name.
        :param query: The query string used for filtering the regions
        :type query: str
        :return: A query for all matching objects
        :rtype: ~django.db.models.QuerySet
        """
        return cls.objects.filter(name__icontains=query)

    @cached_property
    def imprint(self):
        """
        This property returns this region's imprint

        :return: The imprint of this region
        :rtype: ~integreat_cms.cms.models.pages.imprint_page.ImprintPage
        """
        return self.imprints.first()

    @property
    def deepl_budget(self):
        """
        Calculate the maximum translation credit budget (number of words)

        :return: The region's total DeepL budget
        :rtype: int
        """
        # All regions which did not book the add-on get the free credits
        if not self.deepl_addon_booked:
            return settings.DEEPL_CREDITS_FREE
        # All regions which did book the add-on, but not mid-year, get the add-on credits
        if not self.deepl_midyear_start_month:
            return settings.DEEPL_CREDITS_ADDON
        # All regions which booked the add-on in mid-year get a fraction of the add-on credits
        # Calculate how many months lie between the renewal month and the start month of the add-on
        months_difference = self.deepl_renewal_month - self.deepl_midyear_start_month
        # Calculate the available fraction of the add-on
        multiplier = (months_difference % 12) / 12
        return int(multiplier * settings.DEEPL_CREDITS_ADDON)

    @property
    def deepl_budget_remaining(self):
        """
        Calculate the remaining translation credit budget (number of words)

        :return: The region's remaining DeepL budget
        :rtype: int
        """
        return max(0, self.deepl_budget - self.deepl_budget_used)

    @cached_property
    def backend_edit_link(self):
        """
        This function returns the absolute url to the edit form of this region

        :return: The url
        :rtype: str
        """
        return reverse(
            "edit_region",
            kwargs={
                "slug": self.slug,
            },
        )

    def __str__(self):
        """
        This overwrites the default Django :meth:`~django.db.models.Model.__str__` method which would return ``Region object (id)``.
        It is used in the Django admin backend and as label for ModelChoiceFields.

        :return: A readable string representation of the region
        :rtype: str
        """
        label = escape(self.full_name)
        if self.status == region_status.HIDDEN:
            # Add warning if region is hidden
            label += " (&#9888; " + gettext("Hidden") + ")"
        elif self.status == region_status.ARCHIVED:
            # Add warning if region is archived
            label += " (&#9888; " + gettext("Archived") + ")"
        # mark as safe so that the warning triangle is not escaped
        return mark_safe(label)

    def get_repr(self):
        """
        This overwrites the default Django ``__repr__()`` method which would return ``<Region: Region object (id)>``.
        It is used for logging.

        :return: The canonical string representation of the region
        :rtype: str
        """
        return f"<Region (id: {self.id}, slug: {self.slug})>"

    class Meta:
        #: The verbose name of the model
        verbose_name = _("region")
        #: The plural verbose name of the model
        verbose_name_plural = _("regions")
        #: The default permissions for this model
        default_permissions = ("change", "delete", "view")
        #: The default sorting for this model
        ordering = ["name"]
