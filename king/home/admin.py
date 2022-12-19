from django.contrib import admin
from .models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
  list_per_page = 6
  
  list_display = ['sname','reg_no','address','taluka','district','state','photo','pincode']

  def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Student,StudentAdmin)

class MarksAdmin(admin.ModelAdmin):
  list_per_page = 6
  
  list_display = ['reg_no','subject','marks','semester','year']

  def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Marks,MarksAdmin)

class AdmissionAdmin(admin.ModelAdmin):
  list_per_page = 6
  
  list_display = ['reg_no','sname','class_room','branch','year','doadmission','semester']

  def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Admission,AdmissionAdmin)


class FeedbackAdmin(admin.ModelAdmin):
  list_per_page = 6
  
  list_display = ['reg_no','date','subject','feedback_message']

  def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
        
admin.site.register(Feedback,FeedbackAdmin)

