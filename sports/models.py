from django.db import models


class sports(models.Model):
    date= models.DateField(auto_now_add=True)
    head= models.CharField(max_length=500)
    sub= models.CharField(max_length=10000)
    img= models.ImageField(upload_to= 'static/images')