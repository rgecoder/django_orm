from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("This is the Home Page of books/authors")