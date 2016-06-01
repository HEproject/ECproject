from django.db import models
from django.contrib.auth.models import User

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
    
class UserProfile(models.Model):
    # A required line - links a UserProfile to User.
    user = models.OneToOneField(User)
    # SEX_CHO = (('M', 'Male'), ('F', 'Female'))
    # PROVIN_CHO = (('BJ', 'beijin'), ('TJ', 'tianjin'), ('HB', 'hebei'))
    usr_id = models.CharField(max_length=128, default=''   '')
    address = models.CharField(max_length=200, blank=True, default=''   '')
    # privance_id = models.CharField(max_length=2, blank=True,
    #                                choices=PROVIN_CHO, default='   ')
    # The additional attributes we wish to include.
    # usr_sex = models.CharField(max_length=2, choices=SEX_CHO, default='M')
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username


