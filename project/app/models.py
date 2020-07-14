from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_info(models.Model):
    user_data = models.OneToOneField(User,on_delete=models.CASCADE)
    portflio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user_data.username
    
