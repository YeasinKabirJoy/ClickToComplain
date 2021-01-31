from django.db import models

# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag_name

class Info(models.Model):
    #name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    phone_no = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.id)

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return str(self.question)

