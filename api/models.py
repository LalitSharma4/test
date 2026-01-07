from django.db import models

# Create your models here.

from django.db import models

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,UserManager
# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=255)
    mobileNo = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'

    objects=UserManager()

    class Meta:
        db_table = "USER"

class Item(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "ITEMS"