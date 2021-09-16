from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def number_of_blogs(self):
        return self.blogs.filter(is_active=True).count()