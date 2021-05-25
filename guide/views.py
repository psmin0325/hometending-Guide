from django.shortcuts import render
from django.http import HttpResponse
from .models import baseAlchohol
from django.shortcuts import render

def index(request):
    """
    기주 목록 출력
    """
    #return HttpResponse("안녕하세요. 홈텐딩 길라잡이에 오신것을 환영합니다.")
    return render(request, 'guide/baseAlchohol_list.html')

def support(request):
    """
    support 목록 출력
    """
    return render(request, 'guide/secondAlchohol_list.html')

