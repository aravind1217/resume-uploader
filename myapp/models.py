from django.db import models

STATES = (
 
 ('Andhra Pradesh','Andhra Pradesh'),
 ('Delhi','Delhi'),
 ('Goa','Goa'),
 ('Gujarat','Gujarat'),
 ('Karnataka','Karnataka'),
 ('Kerala','Kerala'),
 ('Maharashtra','Maharashtra'),
 ('Puducherry','Puducherry'),
 ('Punjab','Punjab'),
 ('Rajasthan','Rajasthan'),
 ('Tamil Nadu','Tamil Nadu'),
 ('Telangana','Telangana'),
 ('Uttar Pradesh','Uttar Pradesh'),
 
)


class Resume(models.Model):
 name = models.CharField(max_length=100)
 dob = models.DateField(auto_now=False, auto_now_add=False)
 gender = models.CharField(max_length=100)
 city = models.CharField(max_length=100)
 pincode = models.PositiveIntegerField()
 state = models.CharField(choices=STATES, max_length=50)
 mobile = models.PositiveIntegerField()
 email = models.EmailField()
 job_city = models.CharField(max_length=50)
 profile = models.ImageField(upload_to='uploads', blank=True)
 files = models.FileField(upload_to='doc', blank=True)
