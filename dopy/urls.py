from django.conf.urls import include, url,patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from homePage.views import *
from upload.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'dopy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', home),
    url(r'^$',home),
    url(r'^about$', about),
    url(r'^contact$', contact),
    url(r'^gallery$', gallerylist),
    url(r'^gallery/', gallery),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^services/', include('services.urls')),
]
# admin.site.site_header = 'DOPY ADMIN'
# admin.site.site_title = 'DoPy'

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)