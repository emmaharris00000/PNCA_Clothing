from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')

def gallery(request):
    return render(request, 'gallery.html')  

def essay(request):
    return render(request, 'essay.html')  

def contact(request):
    return render(request, 'contact.html')

def clothing(request):
    return render(request, 'clothing.html')

def about(request):
    return render(request, 'about.html')