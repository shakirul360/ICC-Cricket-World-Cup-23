from django.urls import path
from teams import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.teams, name = 'teams'),
    path('teams/<int:team_id>/', views.team_detail, name='team_detail'),

]
    


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)