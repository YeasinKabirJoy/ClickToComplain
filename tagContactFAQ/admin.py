from django.contrib import admin
from .models import Info, FAQ, Tag

admin.site.register([Tag, Info, FAQ])


