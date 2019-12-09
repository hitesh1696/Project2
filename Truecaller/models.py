from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import User
class Contact(models.Model):

    name = models.CharField(max_length=255)
    mobile = models.IntegerField()
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_breed(self):
        return self.name + ' belongs to ' + self.mobile + ' mobile.'

    def __repr__(self):
        return self.name + ' is added.'

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('missing email')
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        #for this example, nothing special happens here
        return self.create_user(email, password)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        max_length=254,
        unique=True,
        db_index=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def get_short_name(self):
        return self.email
    def get_full_name(self):
        return self.email