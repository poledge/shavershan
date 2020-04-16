from django.contrib import admin
from .models import *

class table_passAdmin(admin.ModelAdmin):
    list_display = [field.name for field in table_pass._meta.fields]

    class Meta:
        model = table_pass

admin.sites.site.register(table_pass, table_passAdmin)

class feedAdmin(admin.ModelAdmin):
    list_display = [field.name for field in feed._meta.fields]

    class Meta:
        model = feed

admin.sites.site.register(feed, feedAdmin)

class orderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in order._meta.fields]

    class Meta:
        model = order

admin.sites.site.register(order, orderAdmin)

# Register your models here.
