from django.db import models

# Create your models here.
class Subject(models.Model):
    uid = models.IntegerField(default=0, unique=True)
    name = models.CharField(max_length=20, unique=True)
    secret = models.CharField(max_length=20)
    sex = models.IntegerField(1)
    realname = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    province = models.CharField(max_length=20)
    town = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    adress = models.CharField(max_length=20)
    

    def __unicode__(self):  
        return self.name
