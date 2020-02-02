from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse, request
import datetime as dt

from .models import Image,Category,Location

# Create your views here.

def all_photos(request):
    gallery = Image.get_images()
    locations = Location.get_location()
    return render(request, 'all-pics/index.html', {"gallery": gallery, "locations":locations})


def get_locations(request):
    locations = Location.get_location()

    return render(request, 'navbar.html', {"locations":locations})


def single_image(request, image_id):
    try:
        gallery = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()

    locations = Location.get_location()
    return render(request, 'all-pics/img.html', {"gallery":gallery, 'locations':locations})

def search_results(request):
    try:
        locations = Location.get_location()

        if 'category' in request.GET and request.GET['category']:
            search_term = request.GET.get('category')
            searched_categ = Category.search_category(search_term)
            message = f'{search_term}'

            searched_image = Image.get_pics_cat(searched_categ)

            return render(request, 'all-pics/search.html', {'message': message, 'photo':searched_image, 'locations':locations})

        else:
            message = 'You haven\'t searched for any item'
            return render(request, 'all-pics/search.html', {'message':message})
    except:
        
        return render(request, 'all-pics/search.html', {'locations':locations})

def location_pics(request,loct_id):
    locations = Location.get_location()
    location = Location.objects.filter(id = loct_id)
    pics_by_location = Image.photos_by_loct(loct_id)

    return render(request, 'all-pics/location.html', {'pics_by_location':pics_by_location, 'location':location, 'locations':locations})


def my_image(request, image_id):
    gallery = Image.objects.get(id = image_id)
    image = gallery.image.url
    print(image)
    image_data = open("/path/to/my/"+image, "rb").read()
    
    return HttpResponse(image_data, mimetype="image/png")