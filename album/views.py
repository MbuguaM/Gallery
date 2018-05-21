from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.
def Landing(request):
    """ rendering the landing page """
    images = Image.objects.all()
    return render(request,'main_templates/landing.html',{'images':images})

def details(request, image_id):
    """ rendering image details """
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'main_templates/detail.html', {'image': image})

def search(request):
    """ rendering all the searched images  """
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_image_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'main_templates/search.html', {"message": message, "searched_images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'main_templates/search.html',{"message":message})