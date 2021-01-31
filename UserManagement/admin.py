from django.contrib import admin
from .models import Profile, RegisteredEmail
# Register your models here.
admin.site.register([RegisteredEmail, ])
