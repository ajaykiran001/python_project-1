from django.urls import path
from . import views
app_name='coach'
urlpatterns=[
    path('coach',views.coach,name='coach'),
    path('playerlist',views.playerlist,name='playerlist')
]