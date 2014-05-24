_XOOPS = lambda obj: obj._meta.app_label in ['xoops',]

class SitesRouter(object):

    def db_for_read(self, model, **hints):
        if _XOOPS(model):
            return 'xoops'
        return 'default'


    def db_for_write(self, model, **hints):
        if _XOOPS(model):
            return 'xoops'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        check = [_XOOPS(obj1), _XOOPS(obj2)]

        if all(check):
            return 'xoops'

        if any(check):
            return None

        return 'default'

    def allow_syncdb(self, db, model):
        if _XOOPS(model):
            return 'xoops'

        return 'default'
