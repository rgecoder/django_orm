from django.db import models

class Book(models.Model):
  name = models.CharField(max_length=255)
  desc = models.TextField()
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.name

class Author(models.Model):
  first_name = models.CharField(max_length=255)
  email = models.EmailField()
  books = models.ManyToManyField(Book, related_name='authors')
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  notes = models.CharField(max_length=255, default="Temp")

  def __str__(self):
    return self.first_name