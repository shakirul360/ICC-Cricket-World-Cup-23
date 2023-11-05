from django.urls import path
from player import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.players, name = 'players'),
    # path('venues/<int:venue_id>/', views.venue_detail, name='venue_detail')
    path('players/<int:player_id>/', views.player_info, name='player_inf')

]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)