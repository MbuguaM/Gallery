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
    return render(request, 'galleria/details.html', {'image': image})
