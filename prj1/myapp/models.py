from django.db import models


# Create your models here.


class usr_profile(models.Model):

    username= models.CharField(max_length=255, blank=False, null=False,primary_key=True)	
    fname = models.CharField(max_length=255, blank=False, null=False)
    lname = models.CharField(max_length=255, blank=False, null=False)
    gender = models.CharField(max_length=255, blank=False, null=False)
    email_id = models.EmailField(max_length=255, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    mobile_number = models.IntegerField(blank=False, null=False)
    designation = models.CharField(max_length=255, blank=False, null=False)
    created_datetime = models.DateTimeField(auto_now=True)
    


class audit_log(models.Model):
    log_id= models.AutoField(primary_key=True)
    username= models.ForeignKey(usr_profile,on_delete=models.CASCADE)	
    last_login = models.DateTimeField(auto_now=True )
    activity= models.CharField(max_length=255, blank=False, null=False)
    message= models.CharField(max_length=255, blank=False, null=False)
    

class monitor(models.Model):
    mon_id= models.AutoField(primary_key=True)
    plantname= models.CharField(max_length=255, blank=False, null=False)
    category= models.CharField(max_length=255, blank=False, null=False)
    humidity = models.CharField(max_length=255, blank=False, null=False)
    water_temp= models.CharField(max_length=255, blank=False, null=False)
    ph = models.CharField(max_length=255, blank=False, null=False)
    motor_status = models.BooleanField(default='Not Found')
    light_status = models.BooleanField(default='Not Found')	
    
    
