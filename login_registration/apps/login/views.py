from django.shortcuts import render, redirect
from django.contrib import messages
import re
import bcrypt
from .models import *
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Create your views here.


def index(request):

    return render(request, 'login/index.html')


def register(request):
    error = False
    # validations
    if len(request.POST['first_name']) < 2:
        messages.error(request, "first name must be 2 or more char")
        error = True
    if len(request.POST['last_name']) < 2:
        messages.error(request, "last name must be 2 or more char")
        error = True
    if len(request.POST['password']) < 8:
        messages.error(request, "password must be 8 or more characters")
        error = True
    if request.POST['password'] != request.POST['c_password']:
        messages.error(request, "passwords do not match")
        error = True
    if not EMAIL_REGEX.match(request.POST['email']):
        messages.error(request, "email is invalid")
        error = True
    if len(User.objects.filter(email=request.POST['email'])) > 0:
        messages.error(request, "email already exists")
        error = True
    if error:
        return redirect('/')
    else:
        # create user
        # store user in session
        # redirect to success.html (logged in portion)
        hashed_pw = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt())

        the_user = User.objects.create(
            first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_pw)

        print(the_user)

        request.session['user_id'] = the_user.id

        return redirect('/')


def login(request):
    # alternative method
    # the_user_list = User.objects.filter(email=request.POST['email'])  # [{} {}]
    # if len(the_user_list) > 0:
    #     the_user = the_user_list[0]
    # else:
    #   messages.error(request, "Email or password invalid")
    #   return redirect ('/')
    try:
      the_user = User.objects.get(email = request.POST['email'])
      
    except:
      messages.error(request, "Email or password invalid")
      return redirect ("/")

    #password check
    if bcrypt.checkpw(request.POST['password'].encode(), the_user.password.encode()):
      request.session['user_id'] = the_user.id
    else:
      messages.error(request,"Email or password invalid")
    
    return redirect('/success')

def success(request):
  if not "user_id" in request.session:
    messages.error(request,"Must be logged in to view")
    return redirect('/')
  context = {
    'user': User.objects.get(id = request.session['user_id'])
  }
  return render(request, 'login/success.html', context)

def logout(request):
  request.session.clear()
  return redirect('/')
