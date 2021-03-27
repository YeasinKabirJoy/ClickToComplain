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
from tagContactFAQ import views as tagView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',complainView.homepage, name = 'home'),
    path('registration/', userMangementView.registration, name='registration'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', userMangementView.show_profile, name='profile'),
    path('verify_profile/', userMangementView.send_email, name='send_mail'),
    path('email_verification/', userMangementView.verify_email, name='verification'),
    path('submit_complain/', complainView.complainForm, name = 'submitcompalin'),
    path('complain_list/', complainView.showComplain, name = 'complainList'),
    path('complain_list/<int:complain_id>',complainView.complainDetails, name = 'complainDetails'),
    path('solvedComplainList/', complainView.showSolvedComplain, name='showSolvedComplains'),
    path('solvedComplainList/<int:complain_id>',complainView.complainDetails, name = 'solvedComplainDetails'),
    path('info/',tagView.info, name= 'info'),
    path('faq/',tagView.showFAQ, name= 'faq'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "C2C Admin"
admin.site.site_title = "C2C Admin"
admin.site.index_title = "Welcome to Click To Complian Admin"




# task
# 1.email verification design
# 2.home page
# 3.info
# 4.chart
#5.searching