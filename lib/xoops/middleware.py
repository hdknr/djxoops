from django.contrib import auth
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from xoops.utils import create_user_from

import logging
import traceback
logger = logging.getLogger()

FOLLOW = getattr(settings, 'XOOPS_FOLLOW_LOGOFF', True)
FOLLOW_ONLY_USERS =  getattr(settings, 'XOOPS_FOLLOW_ONLY_USERS', False)

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

        if request.user.is_authenticated():
            if request.user.is_staff or request.user.is_superuser:
                if FOLLOW_ONLY_USERS:
                    return
            elif not FOLLOW:
                return

        try:
            sess_id = request.COOKIES[self.COOKIE_KEY]
            user = create_user_from(sess_id=sess_id)
            if user:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                auth.login(request, user)
                return
        except:
            logger.debug(traceback.format_exc())
            pass

        if FOLLOW:
            auth.logout(request)

