from django.contrib import admin
from django.apps import apps


for model in apps.get_app_config('xoops').get_models():
    admin_class = type(
        "%sAdmin" % model.__name__,
        (admin.ModelAdmin,),
        dict(list_display=tuple([f.name for f in model._meta.fields]),)
    )

    admin.site.register(model, admin_class)
