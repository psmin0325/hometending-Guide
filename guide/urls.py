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

    path('rum/water', views.r_water, name='r_water'),
    path('rum/water/sugar_result', views.rws_result, name='r_w_sugar_result'),

    path('rum/limejuice/', views.r_limejuice, name='r_limejuice'),
    path('rum/limejuice/sugar_result', views.rls_result, name='r_l_sugar_result'),

    path('rum/gingerbeer/', views.rg_result, name='r_g_result'),

    path('rum/pineapple/', views.r_pineapple, name='r_pineapple'),
    path('rum/pineapple/coconut_result/', views.rpc_result, name='r_p_coconut_result'),

    path('gin/', views.gin, name='gin'),
    path('gin/limejuice/', views.g_limejuice, name='g_limejuice'),
    path('gin/limejuice/sugar_result/', views.gls_result, name='g_l_sugar_result'),
    path('gin/limejuice/sparkling_result/', views.glsp_result, name='g_l_sparkling_result'),
    path('gin/limejuice/cider_result/', views.glc_result, name='g_l_cider_result'),
    path('gin/limejuice/tonic_result/', views.glt_result, name='g_l_tonic_result'),

    path('gin/grapefruit/', views.ggf_result, name='ggf_result'),

    path('gin/gingerbeer/', views.g_gingerbeer, name='g_gingerbeer'),
    path('gin/gingerbeer/sparkling_result/', views.ggs_result, name='g_g_sparkling_result'),

    path('whisky/', views.whisky, name='whisky'),
    path('whisky/coffee/', views.w_coffee, name='w_coffee'),
    path('whisky/coffee/whipping_result/', views.wcw_result, name='w_c_whipping_result'),

    path('whisky/sparkling/', views.w_sparkling, name='w_sparkling'),
    path('whisky/sparkling/sugar_result/', views.wss_result, name='w_s_sugar_result'),

    path('whisky/cola_result/', views.wc_result, name='wc_result'),

    path('tequila/', views.tequila, name='tequila'),
    path('tequila/orangejuice/', views.t_orangejuice, name='t_orangejuice'),
    path('tequila/orangejuice/grenadine_result', views.tog_result, name='t_o_grenadine_result'),

    path('tequila/lemonjuice/', views.t_lemonjuice, name='t_lemonjuice'),
    path('tequila/lemonjuice/pineapple_result', views.tlp_result, name='t_l_pineapple_result'),
    path('tequila/lemonjuice/sugar_result', views.tls_result, name='t_l_sugar_result'),

    path('tequila/limejuice/', views.t_limejuice, name='t_limejuice'),
    path('tequila/limejuice/grenadine_result', views.tlg_result, name='t_l_grenadine_result'),
    path('tequila/limejuice/cola_result', views.tlc_result, name='t_l_cola_result'),
]