from django.shortcuts import render, redirect, get_object_or_404
from .models import Food
from django.utils import timezone
# Create your views here.

def food(request):
    foods = Food.objects #쿼리셋= 모델을 오브젝트의 목록을 가져온다고 생각,  메소드
    return render(request,'food.html', {'foods':foods})

def detail(request, food_id):
    details = get_object_or_404(Food, pk = food_id)
    return render(request, 'detail.html', {'details' : details})

def new(request):
    return render(request, 'new.html')      

def create(request):
    food = Food()
    food.author = request.GET['author']
    food.title = request.GET['title'] #get과 post의 차이는 ppt에서 참고
    food.body = request.GET['body']
    food.pub_date = timezone.datetime.now()
    food.created_date = timezone.datetime.now()
    food.save() #쿼리 메소드
    return redirect('food')

 #CRUD의 U인데 edit 수정할 게시글을 가져오는 부분
def edit(request, food_id):
    food = get_object_or_404(Food, pk = food_id)
    return render(request, 'edit.html', {'food' : food})

#CRUD의 U 수정을 하고 다시 저장하는 부분 
def update(request, food_id):
    food = get_object_or_404(Food, pk = food_id)
    food.author = request.GET['author']
    food.title = request.GET['title'] #get과 post의 차이는 ppt에서 참고
    food.body = request.GET['body']
    food.pub_date = timezone.datetime.now()
    food.created_date = timezone.datetime.now()
    food.save() #쿼리 메소드
    return redirect('food')

#CRUD의 D 게시글을 삭제하는 부분
def delete(request, food_id):
    food = get_object_or_404(Food, pk = food_id)
    food.delete()#쿼리 메소드
    return redirect('food')
