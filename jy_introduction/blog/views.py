from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def profile(request):
    return render(request, 'profile.html')

def food(request):
    return render(request,'food.html')
