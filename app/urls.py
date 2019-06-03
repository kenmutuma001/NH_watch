from app import views
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf import settings


urlpatterns = [
    url(r'^$', views.register, name='register'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^home/$', views.home, name='home'),
    url(r'^area/(?P<area_id>[0-9])$', views.area, name='area'),
    url(r'^add-business/', views.add_biz, name='add-biz'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
