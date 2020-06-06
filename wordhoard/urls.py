from django.urls import path 
from . import views 

app_name = 'wordhoard'
urlpatterns = [
	path('', views.wordhoard, name='wordhoard')
]