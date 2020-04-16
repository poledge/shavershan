from django.db import models
from django.core import mail
from django.contrib.auth.models import User
import uuid
import qrcode

class table_pass(models.Model):
    password = models.TextField()

    def __str__(self):
        return "%s" % (self.password)


class feed(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default="")
    composition = models.TextField(default="")
    nutrition = models.TextField(default="")
    cost = models.FloatField()
    img = models.ImageField(default=None)

    def get_id(self):
        return "%s" % (self.id)

    def __str__(self):
        return "%s" % (self.name)
        

class order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.ForeignKey(feed, on_delete=models.CASCADE)
    count = models.IntegerField()
    confirmed = models.BooleanField(default=False)

    def cost(self):
        return "%s" % (self.feed.cost * self.count)

# Create your models here.
