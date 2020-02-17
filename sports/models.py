from django.db import models


class sports(models.Model):
    date = models.DateField(auto_now_add=True)
    head = models.CharField(max_length=500)
    sub = models.CharField(max_length=10000)
    img = models.ImageField(upload_to='pics')


class match(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    logo1 = models.ImageField(upload_to='isl')
    logo2 = models.ImageField(upload_to='isl')


class cricket(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    logo1 = models.ImageField(upload_to='ipl')
    logo2 = models.ImageField(upload_to='ipl')


class comment(models.Model):
    class Meta:
        app_label = 'sports'

    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    address = models.CharField(max_length=300)
    message = models.CharField(max_length=300)

class readmore(models.Model):
    image = models.ImageField(upload_to='blog_pics')
    heading = models.CharField(max_length=400)
    discription = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True, blank=True, null=True)

