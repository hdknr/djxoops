# -*- coding: utf-8 -*-
from django.utils.importlib import import_module
from django.utils.translation import ugettext_lazy as _

from . import GenericCommand, SubCommand
from optparse import make_option
import traceback

from xoops.models import XoopsSession
from xoops.utils import unserialize_session
from phpserialize import loads, dumps
from datetime import datetime

class Command(GenericCommand):

    class SessionList(SubCommand):
        name = 'list_session'
        description = _(u'Xoops Session List')

        def run(self, params, **options):
            for ses in XoopsSession.objects.all():
                print ses.sess_id

    class SessionDetail(SubCommand):
        name = 'detail_session'
        description = _(u'Xoops Session Detail')
        args = [ 
            (('sess_id',), dict(nargs=1, help="Session ID(PHPSESSID)")),
        ]  	

        def run(self, params, **options):
	    sess = XoopsSession.objects.get(sess_id=params.sess_id[0])
            print ">>>[%s]\n" %  sess.sess_data, datetime.fromtimestamp(sess.sess_updated)
	    print ">>>", unserialize_session(sess.sess_data)
	
