from django.db import models

# Create your models here.

class Widget(models.Model):
  # id = models.AutoField(primary_key=True,blank=True)
  id = models.IntegerField(primary_key=True,blank=False)
  widget = models.CharField(max_length=1000000,blank=True)
  function = models.CharField(max_length=1000000,blank=True)
  # game = models.ForeignKey('inmodel',on_delete=models.CASCADE,blank=True)
      
  def __str__(self):
    return str(self.id)
  
# class in_model(models.Model):
#       id = models.AutoField(primary_key=True,blank=True)
#       bet = models.CharField(max_length=10000,blank=True)
#       def __str__(self):
#         return str(self.id)