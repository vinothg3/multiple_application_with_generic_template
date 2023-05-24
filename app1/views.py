from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_string(request):
    return HttpResponse('<h1> This is first application web page </h1>')

def app1_render(request):
    return render(request,'app1_render.html')