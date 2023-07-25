from django.db import models


#bu dosya da yapılan her değişiklikten sonra girilmesi gereken komutlar:
# python manage.py makemigrations
# python manage.py migrate


# Create your models here.
class Ogrenci(models.Model):
    isim= models.CharField(max_length=100) #type text
    aciklama= models.TextField(max_length=1000) #textarea
    no=models.IntegerField() #type number

    def __str__(self) :
        return self.isim