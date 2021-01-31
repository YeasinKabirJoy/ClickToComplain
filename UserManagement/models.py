from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    status = models.BooleanField(blank=True,null=True,default=False)

    def __str__(self):
        return self.user.username


class RegisteredEmail(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
