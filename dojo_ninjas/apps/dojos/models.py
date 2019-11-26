from django.db import models

# Create your models here.
class Language(models.Model):
  name = models.CharField(max_length = 10)

  def __str__(self):
    return self.name

class Framework(models.Model):
  name = models.CharField(max_length=10)
  language = models.ForeignKey(Language, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Movie(models.Model):
  name = models.CharField(max_length=10)

  def __str__(self):
    return self.name

class Character(models.Model):
  name = models.CharField(max_length=10)
  movies = models.ManyToManyField(Movie)

  def __str__(self):
    return self.name







class User(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  email = models.EmailField()
  password = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

class Message(models.Model):
  message = models.TextField()
  user = models.ForeignKey(User,related_name="messages")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
  comment = models.TextField()
  user = models.ForeignKey(User)
  message = models.ForeignKey(Message)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)