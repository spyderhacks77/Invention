from django.db import models

# Create your models here.
class Amazon(models.Model):
    name=models.CharField(max_length=50)
    sender=models.CharField(max_length=50)
    url=models.CharField(max_length=500)
    arate=models.CharField(max_length=100)
    message=models.CharField(max_length=500)

class Flipkart(models.Model):
    fname=models.CharField(max_length=50)
    femail=models.CharField(max_length=50)
    furl=models.CharField(max_length=500)
    fprice=models.CharField(max_length=100)
    fmessage=models.CharField(max_length=500)

class Cowin(models.Model):
    cname=models.CharField(max_length=50)
    cemail=models.CharField(max_length=50)
    cage=models.CharField(max_length=3)
    cpincode=models.CharField(max_length=7)
    cmessage=models.CharField(max_length=500)

class Help(models.Model):
    hname=models.CharField(max_length=50)
    hemail=models.CharField(max_length=50)
    hsubject=models.CharField(max_length=100)
    hmessage=models.CharField(max_length=500)

class Register(models.Model):
    rname=models.CharField(max_length=50)
    rage=models.CharField(max_length=3)
    remail=models.CharField(max_length=50)
    rcontact=models.CharField(max_length=12)
    raddress=models.CharField(max_length=200)

class Verify(models.Model):
    num=models.CharField(max_length=6)