from django.shortcuts import render, redirect

from .models import *

# Create your views here.
def home(request):

  context={
    "course_names" : Course.objects.all(),
    "descriptions" : Description.objects.all(),
  }

  return render(request,'course/home.html', context)

def add(request):
  course_add = Course.objects.create(course_name = request.POST['course_name'])
  course_add.save()
  Description.objects.create(description = request.POST['description'], course = course_add )

  return redirect('/')


def delete(request, desc_id):
  Description.objects.get(id=desc_id).delete()

  return redirect('/')

