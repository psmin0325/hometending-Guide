from django.shortcuts import render
from django.http import HttpResponse
#from .models import baseAlchohol
from django.shortcuts import render
from .models import baseAlchohol

def index(request):
    """
    시작화면
    """

    baseAlchol = {"vodka": 0, "rum": 1}
    return render(request, 'guide/main_menu.html')
    #return HttpResponse("안녕하세요. 홈텐딩 길라잡이에 오신것을 환영합니다.")

def baseAlchohol(request):
    """
    기주 목록 출력
    """
    baseAlchol = {"vodka": 0, "rum": 1}
    return render(request, 'guide/baseAlchohol_list.html')

def vodka(request):
    """
    support_vodka 목록 출력
    """
    return render(request, 'guide/support/vodka.html')

def v_orange(request):
    """
    v_orange 목록 출력
    """
    return render(request, 'guide/additives/v_orange.html')

def voi_result(request):
    """
    결과 화면 출력
    """
    return render(request, 'guide/result/voiResult.html')

def v_cranberry(request):
    """
    v_orange 목록 출력
    """
    return render(request, 'guide/additives/v_cranberry.html')

def voc_result(request):
    """
    결과 화면 출력
    """
    return render(request, 'guide/result/vocResult.html')

def rum(request):
    """
    rum 목록 출력
    """
    return render(request, 'guide/support/rum.html')

def r_orange(request):
    """
    r_orange 목록 출력
    """
    return render(request, 'guide/additives/r_orange.html')

def roi_result(request):
    """
    r_orange 목록 출력
    """
    return render(request, 'guide/result/roiResult.html')

def r_cola(request):
    """
    r_orange 목록 출력
    """
    return render(request, 'guide/additives/r_cola.html')

def rcl_result(request):
    """
    r_orange 목록 출력
    """
    return render(request, 'guide/result/rclResult.html')
