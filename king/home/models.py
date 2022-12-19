from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Student(models.Model):   
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
  sname=models.CharField(max_length=20,blank=True,null=True,default="KunXXXX")
  reg_no=models.CharField(max_length=20,blank=True,null=True,default="20XXX00X")
  address=models.CharField(max_length=20,blank=True,null=True,default="Nanded")
  taluka=models.CharField(max_length=20,blank=True,null=True,default="Nanded")
  district=models.CharField(max_length=20,blank=True,null=True)
  state=models.CharField(max_length=20,blank=True,null=True)
  photo = models.ImageField(upload_to='uploads')
  pincode=models.IntegerField(blank=True,null=True)

  def __str__(self):
    return str(self.reg_no) 
    return str(self.sname) 

class Marks(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
  reg_no=models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
  subject=models.CharField(max_length=20,blank=True,null=True)
  marks=models.IntegerField(blank=True,null=True)
  semester=models.CharField(max_length=20,blank=True,null=True)
  year=models.DateField()

class Admission(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
  reg_no=models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
  sname=models.CharField(max_length=20,blank=True,null=True)
  class_room=models.CharField(max_length=20,blank=True,null=True)
  branch=models.CharField(max_length=20,blank=True,null=True)
  year=models.DateField()
  doadmission=models.DateField()
  semester=models.CharField(max_length=20,blank=True,null=True)

class Feedback(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
  reg_no = models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
  date =models.DateField()
  subject =models.CharField(max_length=20,blank=True,null=True)
  feedback_message = models.CharField(max_length=200,blank=True,null=True)


