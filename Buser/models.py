from django.db import models

# Create your models here.
class Subject(models.Model):
    user_id = models.IntegerField(default=0, unique=True)
    user_name = models.CharField(max_length=20, unique=True)
    user_passwd = models.CharField(max_length=20)
    sex = models.IntegerField(1)
    real_name = models.CharField(max_length=20)
    register_date = models.DateField(auto_now_add=True)
    province = models.CharField(max_length=20)
    town = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    

    def __unicode__(self):  
        return self.name
