import datetime
import json
import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.http import JsonResponse
from django.utils.translation import gettext as _
from django.views.generic import View
from webauthn import base64url_to_bytes, verify_authentication_response
from webauthn.helpers.exceptions import InvalidAuthenticationResponse
from webauthn.helpers.structs import AuthenticationCredential

logger = logging.getLogger(__name__)


class MfaVerifyView(View):
    """
    Verify the response to the challenge generated in :class:`~integreat_cms.cms.views.authentication.mfa.mfa_assert_view.MfaAssertView`.
    After a successful verification, the user is logged in.
    """

    def post(self, request):
        """

        :param request: The current request
        :type request: ~django.http.HttpRequest

        :return: The mfa challenge as JSON
        :rtype: ~django.http.JsonResponse
        """

        if "mfa_user_id" not in request.session:
            return JsonResponse(
                {"success": False, "error": _("You need to log in first")}, status=403
            )

        user = get_user_model().objects.get(id=request.session["mfa_user_id"])

        challenge = request.session["challenge"]
        assertion_response = json.loads(request.body)
        credential_id = assertion_response["id"]

        key = user.mfa_keys.get(key_id=base64url_to_bytes(credential_id))

        try:
            authentication_verification = verify_authentication_response(
                credential=AuthenticationCredential.parse_raw(request.body),
                expected_challenge=base64url_to_bytes(challenge),
                expected_rp_id=settings.HOSTNAME,
                expected_origin=settings.BASE_URL,
                credential_public_key=key.public_key,
                credential_current_sign_count=key.sign_count,
            )
        except InvalidAuthenticationResponse as e:
            logger.exception(e)
            return JsonResponse(
                {"success": False, "error": "Authentication rejected"}, status=403
            )

        # Update counter.
        key.sign_count = authentication_verification.new_sign_count
        key.last_usage = datetime.datetime.now()
        key.save()

        auth_login(request, user, backend="django.contrib.auth.backends.ModelBackend")

        return JsonResponse({"success": True})
