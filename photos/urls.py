from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns=[
    path('',views.all_photos,name='allPhotos'),
    path('image/<image_id>/',views.single_image,name ='image'),
    path('search/', views.search_results, name='search_results'),
    path('location/<loct_id>/', views.location_pics, name='location'),
    path('link/<id>/', views.my_image, name='link' )
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
