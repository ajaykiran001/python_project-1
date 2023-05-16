from django.urls import path
from . import views
app_name='fans'
urlpatterns=[
    path('home',views.home,name='home')
]