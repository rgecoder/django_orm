from __future__ import unicode_literals
from django.shortcuts import render, redirect

from .models import *

# Create your views here.
def index(request):
  print (User.objects.all())
  context = {
    "users" : User.objects.all(),
  }
  return render(request,'semi_users/index.html', context)

def new_page(request):
  return render(request,'semi_users/new.html')

def create(request):
  
  User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email']),
  
  return redirect('/')
  

def show(request, user_id):
  
  context = {
    "user" : User.objects.get(id = user_id),

  }
  

  return render(request, 'semi_users/show.html', context)
  

def edit(request, user_id):
  context = {
    "user": User.objects.get(id = user_id),
  }

  return render(request, 'semi_users/edit.html', context)

def delete(request, user_id):
  User.objects.get(id=user_id).delete()

  return redirect('/')
  

def update(request):
  
  user = User.objects.get(id=request.POST['user_id'])

  user.first_name = request.POST['first_name']
  user.last_name = request.POST['last_name']
  user.email = request.POST['email']
  
  user.save()


  return redirect('/')


