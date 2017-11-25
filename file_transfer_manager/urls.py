"""edc_sync_file_monitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from edc_base.views import LogoutView, LoginView

from .admin_site import file_transfer_monitor_admin
from .views import ReportView, HomeView


app_name = 'file_transfer_manager'

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^file_monitor_admin/', file_transfer_monitor_admin.urls),
    url(r'^edc/', include('edc_base.urls')),
    url(r'login', LoginView.as_view(), name='login_url'),
    url(r'^tz_detect/', include('tz_detect.urls')),
    url(r'logout', LogoutView.as_view(
        pattern_name='login_url'), name='logout_url'),
    url(r'^report/(?P<site_value>\w+)/$',
        ReportView.as_view(), name='report_url'),
    url(r'', HomeView.as_view(), name='home_url'),
]
