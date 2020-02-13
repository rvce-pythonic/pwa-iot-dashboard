from django.db import models

# Create your models here.
class profile(models.Model):
	username = models.CharField(primary_key=True,max_length=10,blank=False,null=False)
	password = models.CharField(max_length=10,blank=False,null=False)
	name = models.CharField(max_length=20,blank=False,null=False)
	dob = models.DateField()
	email = models.EmailField(blank=False,null=False)
	phone = models.BigIntegerField(blank=False,null=False)
	address = models.CharField(max_length=20)

class audit(models.Model):
	a_id = models.AutoField(primary_key=True)
	username = models.ForeignKey(profile,on_delete=models.CASCADE)
	login = models.DateTimeField(null=False,blank=False)
	logout =  models.DateTimeField(null=True,blank=True)

class aquaponics:
	temp = models.FloatField(max_length=4,default='None')
	humidity = models.FloatField(max_length=4,default='None')
	ph = models.FloatField(max_length=4,default='None')
	f_waterLevel = models.FloatField(max_length=4,default='None')
	b_waterlevel = models.FloatField(max_length=4,default='None')
	light_state = models.BooleanField(default='None')
	motor_state = models.BooleanField(default='None')
	water_temp = models.BooleanField(default='None')

