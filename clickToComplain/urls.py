"""clickToComplain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from UserManagement import views as userMangementView
from Complain import views as complainView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', userMangementView.registration, name='registration'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', userMangementView.show_profile, name='profile'),
    path('verify_profile/', userMangementView.send_email, name='send_mail'),
    path('email_verification/', userMangementView.verify_email, name='verification'),
    path('submit_complain/', complainView.complainForm, name = 'submitcompalin'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
