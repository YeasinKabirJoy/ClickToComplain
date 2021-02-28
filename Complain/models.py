from django.db import models
from django.contrib.auth.models import User
from tagContactFAQ.models import Tag
from vote.models import VoteModel



class Comment(models.Model):

    comment = models.TextField(blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user)



# Create your models here.
class Complain(VoteModel, models.Model):
    image = models.ImageField(upload_to='complain/image', blank=True,null=True)
    status = models.CharField(max_length=100, choices=(('Pending', 'Pending'),('Solved', 'Solved')), default='Pending')
    description = models.TextField()
    tag = models.ManyToManyField(Tag, blank=True)
    private = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ManyToManyField(Comment, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = ('')
