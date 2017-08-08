"""archiver_system URL Configuration

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
from archiver.views.link import redirect_link_archive, redirect_link_original

from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^/l/?$', link_create),
    url(r'^l/(?P<identifier>[0-9A-Fa-f]{32})/?$', redirect_link_original),
    url(r'^l/(?P<identifier>[0-9A-Fa-f]{32})/archive/?$', redirect_link_archive)
    #url(r'^l/(?P<identifier>[0-9A-Fa-f]{32})/meta/?$', redirect_link_meta),
    #url(r'f/$', file_create),
    #url(r'f/(?P<identifier>[0-9A-Fa-f]*)/?$', file_download)
    #url(r'f/(?P<identifier>[0-9A-Fa-f]*)/meta/?$', file_meta)
]
