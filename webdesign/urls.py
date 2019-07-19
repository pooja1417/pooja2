"""webdesign URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url,include
from . import views as w
from .views import home_page,about_page,home1
from web import views
from web.views import career_view as vw
from web.urls import urlpatterns as web_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page),
    url(r'^about$',w.about_page, name="about_page"),
    url(r'^home$', w.home1,name="home1"),
    url(r'^about/contact$', w.home1,name="home1"),
    url(r'^career$', vw , name="vw"),
    
]

if settings.DEBUG:
	urlpatterns=urlpatterns+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
