from django.db import models

# Create your models here.
class Dojo(models.Model):
  name = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=255)
  desc = models.CharField(max_length=255, default="TEMP")

  def __str__(self):
    return self.name

class Ninja(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  enrolled = models.ForeignKey(Dojo, related_name='ninjas')

  def __str__(self):
    return self.first_name




