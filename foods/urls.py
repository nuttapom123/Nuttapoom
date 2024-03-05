from django.urls import path
from . import views

urlpatterns = [
    path('',views.foods,name='foods'),
    path('food',views.food,name='food')
]