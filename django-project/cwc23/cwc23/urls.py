"""
URL configuration for cwc23 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from venues import views as venues_views
from match import views as match_views
from news import views as news_views

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('venues/',include('venues.urls')),
    path('account/',include('users_app.urls')),
    path('', venues_views.index, name = 'index'),
    path('matches/', match_views.matches, name='matches'),
    path('news/', news_views.lateNews, name='news'),
    #path('account/', include('users.urls'))
    
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

