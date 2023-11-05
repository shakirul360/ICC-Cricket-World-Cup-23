from django.urls import path
from venues import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.venues, name = 'venues'),
    path('venues/<int:venue_id>/', views.venue_detail, name='venue_detail')
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)