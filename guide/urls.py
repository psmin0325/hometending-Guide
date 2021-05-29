from django.urls import path

from . import views

app_name='guide'

urlpatterns = [
    path('', views.index, name='index'),

    path('select/', views.baseAlchohol, name='base'),

    #vodka 영역
    path('vodka/', views.vodka, name='vodka'),
    path('vodka/orange/', views.v_orange, name='v_orange'),
    path('vodka/orange/ice_result', views.voi_result, name='v_o_ice_result'),
    path('vodka/cranberry/', views.v_cranberry, name='v_cranberry'),
    path('vodka/cranberry/cranberry_result', views.voc_result, name='v_o_cranberry_result'),


    #path('vodka/cranberry/', views.v_c_add, name='cranberry'),
    path('rum/', views.rum, name='rum'),
    path('rum/orange/', views.r_orange, name='r_orange'),
    path('rum/orange/ice_result', views.roi_result, name='r_o_ice_result'),
    path('rum/cola/', views.r_cola, name='r_cola'),
    path('rum/cola/lime_result', views.rcl_result, name='r_c_lime_result'),
]