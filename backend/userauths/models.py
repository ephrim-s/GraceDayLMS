from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    full_name = models.CharField(max_length=200)
    otp = models.IntegerField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        email_username, full_name = self.email.split('@')
        if self.full_name == "" or self.full_name == None:
            self.full_name == email_username
        if self.username == "" or self.username == None:
            self.usernam = email_username
        super(User, self).save(*args, **kwargs)

class Profile(models.Model):
    pass