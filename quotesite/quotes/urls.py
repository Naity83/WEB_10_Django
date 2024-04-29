from django.urls import path, include

from . import views

app_name = "quotes"

urlpatterns = [
    path('', views.main, name='root'),  
   
]