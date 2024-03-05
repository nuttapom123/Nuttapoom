from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.


def foods(request):
    
    return render(request,'foods/foods.html')

def food(request):
    return render(request,'foods/food.html')

