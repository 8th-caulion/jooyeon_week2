from django.shortcuts import render, redirect, get_object_or_404
from .models import Travel
from django.utils import timezone
# Create your views here.

def travel(request):
    travels = Travel.objects #쿼리셋= 모델을 오브젝트의 목록을 가져온다고 생각,  메소드
    return render(request,'travel.html', {'travels':travels})

def detail(request, travel_id):
    details = get_object_or_404(Travel, pk = travel_id)
    return render(request, 'detail.html', {'details' : details})

def new(request):
    return render(request, 'new.html')      

def create(request):
    travel = Travel()
    travel.author = request.GET['author']
    travel.title = request.GET['title'] #get과 post의 차이는 ppt에서 참고
    travel.body = request.GET['body']
    travel.pub_date = timezone.datetime.now()
    travel.created_date = timezone.datetime.now()
    travel.save() #쿼리 메소드
    return redirect('travel')

 #CRUD의 U인데 edit 수정할 게시글을 가져오는 부분
def edit(request, travel_id):
    travel = get_object_or_404(Travel, pk = travel_id)
    return render(request, 'edit.html', {'travel' : travel})

#CRUD의 U 수정을 하고 다시 저장하는 부분 
def update(request, travel_id):
    travel = get_object_or_404(Travel, pk = travel_id)
    travel.author = request.GET['author']
    travel.title = request.GET['title'] #get과 post의 차이는 ppt에서 참고
    travel.body = request.GET['body']
    travel.pub_date = timezone.datetime.now()
    travel.created_date = timezone.datetime.now()
    travel.save() #쿼리 메소드
    return redirect('travel')

#CRUD의 D 게시글을 삭제하는 부분
def delete(request, travel_id):
    travel = get_object_or_404(Travel, pk = travel_id)
    travel.delete()#쿼리 메소드
    return redirect('travel')
