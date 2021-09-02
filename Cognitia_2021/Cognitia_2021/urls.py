from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from rest_framework import routers
from api import views
router = routers.DefaultRouter()

router.register('year', views.YearView, basename='year')
router.register('events', views.EventView, basename='events')
router.register('prize', views.PrizeView, basename='prize')
router.register('teammembers', views.TeamMemberView, basename='teammember')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
