import phpserialize
import re
from models import XoopsUsers, XoopsSession
from django.contrib.auth.models import User


def unserialize_session(val):
    ''' https://gist.github.com/scragg0x/3894835

        /etc/php5/apache2/conf.d/suhosin.ini

        suhosin.session.encrypt = off
        suhosin.cookie.encrypt = off
    '''

    if not val:
        return
    session = {}
    groups = re.split("([a-zA-Z0-9_]+)\|", val)
    if len(groups) > 2:
        groups = groups[1:]
        groups = map(None, *([iter(groups)] * 2))

        for i in range(len(groups)):
            session[groups[i][0]] = phpserialize.loads(groups[i][1])
    return session


def create_user_from(xoops_user=None, sess_id=None):
    xoops_user = xoops_user or find_xoops_user(sess_id)
    if not xoops_user:
        return None
    try:
        return User.objects.get(username=xoops_user.uname)
    except User.DoesNotExist:
        user = User.objects.create_user(
            username=xoops_user.uname,
            password=xoops_user.pass_field,
            email=xoops_user.email)
        return user
    return None


def find_xoops_user(sess_id):
    try:
        s = XoopsSession.objects.get(sess_id=sess_id)
        sd = unserialize_session(s.sess_data)
        return XoopsUsers.objects.get(uid=sd['xoopsUserId'])
    except XoopsSession.DoesNotExist:
        return None
    except XoopsUsers.DoesNotExist:
        return None
    return None
