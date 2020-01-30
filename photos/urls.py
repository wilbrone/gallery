from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns=[
    url('^$',views.all_photos,name='allPhotos'),
    url(r'^image/(\d+)',views.single_image,name ='image'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/(\d+)', views.location_pics, name='location')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
