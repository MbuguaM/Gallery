from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.Landing, name ='landing_page'),
    url(r'^details/(?P<image_id>[0-9]+)/$',views.details, name = 'details'),
    url(r'^search/$',views.search, name = "search" )
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)