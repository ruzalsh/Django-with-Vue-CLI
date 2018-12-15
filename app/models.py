from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):

    def create_user(self,name,email,password=None):
        if not email:
            raise ValueError('User must have and email address.')

#Normalize the email address by lowercasing the domain part of it.
        email=self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,name,email,password):
        user = self.create_user(name,email,password)
        user.is_superuser =True
        user.is_staff = True
        user.save(using=self._db)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile"""
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.email


class ProfileFeedItem(models.Model):
    user_profile =models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text


class Post(models.Model):
    user_profile = models.ForeignKey(UserProfile,on_delete= models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    gener = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    published_on = models.DateTimeField(null = True)

    @property
    def comments(self):
        return self.comment_set.all()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    author = models.CharField(max_length=150)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved_on = models.BooleanField(default=False)

    def __str__(self):
        return self.author
