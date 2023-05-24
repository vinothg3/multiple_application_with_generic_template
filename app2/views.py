from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_string(request):
    return HttpResponse('<h1> This second application web page <h1>')

def app2_render(request):
    return render(request,'app2_render.html')