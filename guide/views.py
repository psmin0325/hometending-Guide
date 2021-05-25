from django.shortcuts import render
from django.http import HttpResponse
from .models import baseAlchohol
from django.shortcuts import render

def index(request):
    """
    기주 목록 출력
    """
    baseAlchohol_list = baseAlchohol.img
    #return HttpResponse("안녕하세요. 홈텐딩 길라잡이에 오신것을 환영합니다.")
    return render(request, 'guide/baseAlchohol_list.html')
#     question_list = Question.objects.order_by('-create_date')
#     context = {'question_list': question_list}
# # ---------------------------------- [edit] ---------------------------------- #
#     return render(request, 'pybo/question_list.js', context)
