from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Blog(models.Model):
  name = models.CharField(max_length=255)
  desc = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __repr__(self):
    return "<Blog object: Name:{}  Desc:{}>".format(self.name, self.desc)

class Comment(models.Model):
  comment = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  # 1 to many relationship
  blog = models.ForeignKey(Blog,related_name = "comments")
class Admin(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  # many to many relationship
  blogs = models.ManyToManyField(Blog, related_name = "admins")
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)



