from django.urls import path, include

from . import views

app_name = "quotes"

urlpatterns = [
    path('', views.main, name='root'),  
    path('<int:page>', views.main, name='root_paginate'),
    path('author/<str:author_id>', views.author_about, name='author'),
 
   ]