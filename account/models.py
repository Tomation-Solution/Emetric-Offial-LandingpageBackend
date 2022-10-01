from email.policy import default
from pyexpat import model
from typing import List,Any
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, first_name,last_name, password=None):
        """
        Creates and saves a User with the given email,first_name,last_name and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.is_active = False# would remove this once i fix the email issue
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  first_name,last_name,  password=None):
        """
        Creates and saves a superuser with the given email,first_name,last_name  and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_active=True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):

    email = models.EmailField(unique=True)
    first_name =models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    REQUIRED_FIELDS:List[str] = ['first_name','last_name']
    USERNAME_FIELD:str = 'email'
    objects = UserManager()


    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    def __str__(self) -> str:
        return f'{self.email}'

    def get_full_name(self):
        return f'{self.first_name} f{self.last_name}'



    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        return self.is_superuser