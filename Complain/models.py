from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Complain(models.Model):
    image = models.ImageField(upload_to='complain/image', blank=True,null=True)
    status = models.CharField(max_length=100, choices=(('Pending', 'Pending'),('Solved', 'Solved')), default='Pending')
    description = models.TextField()
    private = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)




    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
