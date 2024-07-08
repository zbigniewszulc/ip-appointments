from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("Hello World! This is Test Page")

def index(request):

   if request.method == "GET":
       return HttpResponse("Hello World! This was a GET request")
   elif request.method == "POST":
       return HttpResponse("Hello World! This was a POST request")
