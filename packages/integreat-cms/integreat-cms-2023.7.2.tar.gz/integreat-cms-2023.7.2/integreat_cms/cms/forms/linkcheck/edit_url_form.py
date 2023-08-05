import logging

from django import forms
from django.core.validators import EmailValidator, URLValidator
from django.utils.translation import gettext as _

logger = logging.getLogger(__name__)


class LinkField(forms.URLField):
    """
    A field for links that might be URLs but could also be mailto: or tel: links
    """

    #: Disable the default URL validator
    default_validators = []
    #: Whether to skip the validation URL fragments in URLField.to_python()
    skip_url_fragment_validation = True

    def to_python(self, value):
        """
        Convert the string value to the appropriate Python data structure for this field

        :param value: The value that was input into the form
        :type value: str

        :returns: The Python value
        :rtype: str
        """
        if self.skip_url_fragment_validation:
            # Skip the URL field to_python for email and phone links
            logger.debug(
                "Value %r is a mailto or tel link, skipping to_python() of URLField.",
                value,
            )
            value = super(forms.URLField, self).to_python(value)
        else:
            value = super().to_python(value)
        return value

    def clean(self, value):
        """
        Validate the given value and return its "cleaned" value as an
        appropriate Python object. Raise ValidationError for any errors.

        :param value: The value that was input into the form
        :type value: str

        :returns: The cleaned value
        :rtype: str
        """
        if value.startswith("mailto:"):
            email = value[7:]
            logger.debug(
                "Value %r is an email link, enforcing EmailValidator on %r",
                value,
                email,
            )
            self.validators.append(EmailValidator())
            self.error_messages["invalid"] = _("Enter a valid email address.")
            value = f"mailto:{super().clean(email)}"
        else:
            if not value.startswith("tel:"):
                logger.debug("Value %r is a normal link, enforcing URLValidator", value)
                self.validators.append(URLValidator())
                self.skip_url_fragment_validation = False
            value = super().clean(value)
        return value


class EditUrlForm(forms.Form):
    """
    Form for creating and modifying Link objects
    """

    url = LinkField()
