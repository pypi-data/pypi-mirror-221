import logging

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from ...decorators import permission_required
from ...forms import RegionFeedbackFilterForm
from ...models import Feedback

logger = logging.getLogger(__name__)


@method_decorator(permission_required("cms.view_feedback"), name="dispatch")
class RegionFeedbackListView(TemplateView):
    """
    View to list all region feedback (content feedback)
    """

    #: The template to render (see :class:`~django.views.generic.base.TemplateResponseMixin`)
    template = "feedback/region_feedback_list.html"
    template_archived = "feedback/region_feedback_list_archived.html"

    #: Whether or not to show archived feedback
    archived = False

    @property
    def template_name(self):
        """
        Select correct HTML template, depending on :attr:`~integreat_cms.cms.views.feedback.region_feedback_list_view.RegionFeedbackListView.archived` flag
        (see :class:`~django.views.generic.base.TemplateResponseMixin`)
        :return: Path to HTML template
        :rtype: str
        """
        return self.template_archived if self.archived else self.template

    def get(self, request, *args, **kwargs):
        r"""
        Render region feedback list

        :param request: Object representing the user call
        :type request: ~django.http.HttpRequest

        :param \*args: The supplied arguments
        :type \*args: list

        :param \**kwargs: The supplied keyword arguments
        :type \**kwargs: dict

        :return: The rendered template response
        :rtype: ~django.template.response.TemplateResponse
        """

        # current region
        region = request.region

        region_feedback = Feedback.objects.filter(
            region=region, is_technical=False, archived=self.archived
        )

        filter_form = RegionFeedbackFilterForm(data=request.GET)
        region_feedback, query = filter_form.apply(region_feedback, region)

        region_feedback = region_feedback.select_related("region", "language")

        chunk_size = int(request.GET.get("size", settings.PER_PAGE))
        paginator = Paginator(region_feedback, chunk_size)
        chunk = request.GET.get("page")
        region_feedback_chunk = paginator.get_page(chunk)

        return render(
            request,
            self.template_name,
            {
                "current_menu_item": "region_feedback",
                "region_feedback": region_feedback_chunk,
                "archived_count": Feedback.objects.filter(
                    region=region, is_technical=False, archived=True
                ).count(),
                "filter_form": filter_form,
                "search_query": query,
            },
        )
