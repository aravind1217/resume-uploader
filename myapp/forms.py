from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Resume
from django.contrib.auth.models import User

GENDER_CHOICES = [
 ('Male', 'Male'),
 ('Female', 'Female')
]

CITY_CHOICE = [
 ('Delhi', 'Delhi'),
 ('Chennai', 'Chennai'),
 ('Kerala', 'Kerala'),
 ('Mumbai', 'Mumbai'),
 ('Coimbatore', 'Coimbatore'),
 ('Banglore', 'Banglore'),
 ('Mysore', 'Mysore')
]

class ResumeForm(forms.ModelForm):
 gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
 job_city = forms.MultipleChoiceField(label='Preferred Job Locations', choices=CITY_CHOICE, widget=forms.CheckboxSelectMultiple)
 class Meta:
  model = Resume
  fields = ['name', 'dob', 'gender',  'city', 'pincode', 'state', 'mobile', 'email', 'job_city', 'profile', 'files']
  labels = {'name':'Full Name', 'dob': 'Date of Birth', 'pincode':'Pin Code', 'mobile':'Mobile No.', 'email':'Email ID', 'profile':'Profile', 'files':'Document'}
  widgets = {
   'name':forms.TextInput(attrs={'class':'form-control'}),
   'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
   
   'city':forms.TextInput(attrs={'class':'form-control'}),
   'pincode':forms.NumberInput(attrs={'class':'form-control'}),
   'state':forms.Select(attrs={'class':'form-select'}),
   'mobile':forms.NumberInput(attrs={'class':'form-control'}),
   'email':forms.EmailInput(attrs={'class':'form-control'}),
  }

class UserForm(UserCreationForm):
    email = forms.EmailField()
    model = User
    fields = ['username','email','password1','password2']