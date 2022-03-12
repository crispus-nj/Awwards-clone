from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class Account(BaseUserManager):
    def create_user(self, username, email, password=None):
        user = self.model(
            username = username,
            email = self.normalize_email(email)
        )
        user.set_password(password)
        
        user.save(using = self._db)
        return user
        
    def create_superuser(self, username, email, password):
        user = self.create_user(
            username = username,
            email = self.normalize_email(email),
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        user.save(using = self._db)

        return user

class UserAccount(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100,unique=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(null=True, default='avatar.svg')

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = Account()

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, add_label):
        return self.is_admin
