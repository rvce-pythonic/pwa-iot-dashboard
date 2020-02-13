from django.db import models

# Create your models here.


class profile(models.Model):

	uname = models.CharField(max_length=255, blank=False, null=False, primary_key=True)
	fname = models.CharField(max_length=255, blank=False, null=False)
	lname = models.CharField(max_length=255, blank=False, null=False)
	DOB = models.DateTimeField(null=True)
	emailId = models.EmailField(max_length=255, blank=False, null=False)
	password = models.CharField(max_length=255, blank=False, null=False)
	phone = models.BigIntegerField( blank=False, null=False)
	address = models.CharField(max_length=255, blank=False, null=False)

class audit_log(models.Model):
	log_Id = models.AutoField(primary_key=True)
	uname = models.ForeignKey(profile, on_delete=models.CASCADE)
	login = models.DateTimeField(blank=False, null=False)
	logout = models.DateTimeField(blank=False, null=False)
	activity = models.CharField(max_length=255, blank=False, null=False)

class hydroponics(models.Model):
	h_id = models.AutoField(primary_key=True)
	plant_name = models.CharField(max_length=255, blank=False, null=False)
	plant_type = models.CharField(max_length=255, blank=False, null=False)
	temperature = models.CharField(max_length=255, blank=False, null=False)
	humidity = models.CharField(max_length=255, blank=False, null=False)
	ph_value = models.CharField(max_length=255, blank=False, null=False)
	motor = models.BooleanField(default='none')
	light = models.BooleanField(default='none')
