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
    path('vodka/orange/grenadine_result', views.vog_result, name='v_o_grenadine_result'),

    path('vodka/cranberry/', views.v_cranberry, name='v_cranberry'),
    path('vodka/cranberry/lime_result', views.vcl_result, name='v_c_lime_result'),
    path('vodka/cranberry/grapefruit_result', views.vcg_result, name='v_c_grapefruit_result'),
    path('vodka/cranberry/limejuice_result', views.vclj_result, name='v_c_limejuice_result'),
    path('vodka/cranberry/orangejuice_result', views.vco_result, name='v_c_orangejuice_result'),

    path('vodka/limejuice_result', views.vlj_result, name='v_limejuice_result'),
    path('vodka/cola_result', views.vc_result, name='v_cola_result'),

    path('vodka/tonic/', views.v_tonic, name='v_tonic'),
    path('vodka/tonic/lime_result', views.vtl_result, name='v_t_lime_result'),

    path('vodka/gingerbeer/', views.v_gingerbeer, name='v_gingerbeer'),
    path('vodka/gingerbeer/lime_result', views.vgl_result, name='v_g_lime_result'),

    #path('vodka/cranberry/', views.v_c_add, name='cranberry'),
    path('rum/', views.rum, name='rum'),
    path('rum/orange/', views.r_orange, name='r_orange'),
    path('rum/orange/ice_result', views.roi_result, name='r_o_ice_result'),
    path('rum/cola/', views.r_cola, name='r_cola'),
    path('rum/cola/lime_result', views.rcl_result, name='r_c_lime_result'),
]