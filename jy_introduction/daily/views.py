from django.shortcuts import render

# Create your views here.
def travel(request):
    return render(request,'travel.html')

def food(request):
    return render(request,'food.html')