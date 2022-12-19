from django.contrib import admin
from django.urls import path, include
# from .views import view_stud_info,view_admission,view_feedback,view_marks
from home import views
# from django.conf.urls.defaults import *

urlpatterns = [
    
    path('student/',views.view_stud_info,name="student"),
    path('marks/',views.view_marks,name="marks"),
    path('admission/',views.view_admission,name="admission"),
    path('feedback/',views.view_feedback,name="feedback"),
    path('view_data/', views.view_data ,name= 'view_data'),
    path('',views.index,name="index") ,

]
