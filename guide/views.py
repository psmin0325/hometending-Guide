from django.shortcuts import render
from django.http import HttpResponse
#from .models import baseAlchohol
from django.shortcuts import render

baseAlc = -1
secondAlc = -1
addi = -1

def index(request):
    """
    기주 목록 출력
    """
    return render(request, 'guide/baseAlchohol_list.html')
    #return HttpResponse("안녕하세요. 홈텐딩 길라잡이에 오신것을 환영합니다.")

def support(request):
    """
    support 목록 출력
    """
    return render(request, 'guide/secondAlchohol_list.html')

def additives(request):
    """
    첨가물 목록 출력
    """
    return render(request, 'guide/additives_list.html')

def result(request):
    """
    결과 화면 출력
    """
    return render(request, 'guide/result.html')