from django.conf.urls import patterns, include, url
from mysite.view.views import current_datetime, hours_ahead

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('', (r'^time/$', current_datetime),
	(r'^time/plus/(\d{1,2})/$', hours_ahead),
)
