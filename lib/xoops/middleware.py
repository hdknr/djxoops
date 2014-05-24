from django.contrib import auth
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from xoops.utils import create_user_from

FOLLOW = getattr(settings, 'XOOPS_FOLLOW_LOGOFF', True)

class AuthMiddleware(object):

    COOKIE_KEY = "PHPSESSID"

    def process_request(self, request):

        # AuthenticationMiddleware is required so that request.user exists.
        if not hasattr(request, 'user'):
            raise ImproperlyConfigured(
                "The Django remote user auth middleware requires the"
                " authentication middleware to be installed.  Edit your"
                " MIDDLEWARE_CLASSES setting to insert"
                " 'django.contrib.auth.middleware.AuthenticationMiddleware'"
                " before the XoopsAuthMiddleware class.")

        if not FOLLOW and request.user.is_authenticated():
            return

        try:
            sess_id = request.COOKIES[self.COOKIE_KEY]
            user = create_user_from(sess_id=sess_id)
            if user:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                auth.login(request, user)
                return
        except:
            pass

        if FOLLOW:
            auth.logout(request)
