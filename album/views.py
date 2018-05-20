from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Landing(request):
    """ rendering the landing page """
    return render(request,'main_templates/landing.html')

