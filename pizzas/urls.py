from django.urls import path    #the path function, which is needed when mapping URLs to views

#the dot tells Python to import the views.py module from the same directory as the current urls.py module.
from . import views 

app_name = 'pizzas'

#The variable urlpatterns in this module is a list of indevidual pages  that can be requested from the pizzas app.
urlpatterns = [
    path('', views.index, name='index'),
    path('pizzas', views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
    path('new_comment/<int:pizza_id>/', views.new_comment, name='new_comment'),
]