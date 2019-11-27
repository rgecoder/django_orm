from django.db import models

# Create your models here.
class Course(models.Model):
  course_name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Description(models.Model):
  description = models.CharField(max_length=255)
  course=models.OneToOneField(Course, related_name="desc")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  


  