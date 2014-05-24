from __future__ import unicode_literals
from django.conf import settings

PFX = getattr(settings, 'XOOPS_PREFIX', 'xoops')

from django.db import models


class XoopsUsers(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    uname = models.CharField(max_length=25)
    email = models.CharField(max_length=60)
    url = models.CharField(max_length=100)
    user_avatar = models.CharField(max_length=30)
    user_regdate = models.IntegerField()
    user_icq = models.CharField(max_length=15)
    user_from = models.CharField(max_length=100)
    user_sig = models.TextField()
    user_viewemail = models.IntegerField()
    actkey = models.CharField(max_length=8)
    user_aim = models.CharField(max_length=18)
    user_yim = models.CharField(max_length=25)
    user_msnm = models.CharField(max_length=100)
    pass_field = models.CharField(db_column='pass', max_length=33)
    posts = models.IntegerField()
    attachsig = models.IntegerField()
    rank = models.IntegerField()
    level = models.IntegerField()
    theme = models.CharField(max_length=100)
    timezone_offset = models.FloatField()
    last_login = models.IntegerField()
    umode = models.CharField(max_length=10)
    uorder = models.IntegerField()
    notify_method = models.IntegerField()
    notify_mode = models.IntegerField()
    user_occ = models.CharField(max_length=100)
    bio = models.TextField()
    user_intrest = models.CharField(max_length=150)
    user_mailok = models.IntegerField()

    class Meta:
        managed = False
        db_table = '%s_users' % PFX


class XoopsSession(models.Model):
    sess_id = models.CharField(primary_key=True, max_length=32)
    sess_updated = models.IntegerField()
    sess_ip = models.CharField(max_length=40)
    sess_data = models.TextField()

    class Meta:
        managed = False
        db_table = '%s_session' % PFX
