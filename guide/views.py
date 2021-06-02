from django.shortcuts import render
from django.http import HttpResponse
#from .models import baseAlchohol
from django.shortcuts import render

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

def vog_result(request):
    """
    결과 화면 출력
    """
    return render(request, 'guide/result/vogResult.html')

def v_cranberry(request):
    """
    v_orange 목록 출력
    """
    return render(request, 'guide/additives/v_cranberry.html')

def vcl_result(request):
    """
    결과 화면 출력
    """
    return render(request, 'guide/result/vclResult.html')

def vcg_result(request):
    """
    결과 화면 출력
    """
    return render(request, 'guide/result/vcgResult.html')

def vclj_result(request):
    """
    결과 화면 출력
    """
    return render(request, 'guide/result/vcljResult.html')

def vco_result(request):
    """
    결과 화면 출력
    """
    return render(request, 'guide/result/vcoResult.html')

def vlj_result(request):
    """
    v_limejuice 목록 출력
    """
    return render(request, 'guide/result/vljResult.html')

def v_tonic(request):
    """
    v_tonic 목록 출력
    """
    return render(request, 'guide/additives/v_tonic.html')

def vtl_result(request):
    """
    결과 화면 출력
    """
    return render(request, 'guide/result/vtlResult.html')

def v_gingerbeer(request):
    """
    v_tonic 목록 출력
    """
    return render(request, 'guide/additives/v_gingerbeer.html')

def vgl_result(request):
    """
    결과 화면 출력
    """
    return render(request, 'guide/result/vglResult.html')

def vc_result(request):
    """
    결과 화면 출력
    """
    return render(request, 'guide/result/vcResult.html')

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

def rcl_result(request):
    """
    r_orange 목록 출력
    """
    return render(request, 'guide/result/rclResult.html')

def r_water(request):
    """
    r_orange 목록 출력
    """
    return render(request, 'guide/additives/r_water.html')

def rws_result(request):
    """
    r_orange 목록 출력
    """
    return render(request, 'guide/result/rwsResult.html')

def r_limejuice(request):
    """
    r_orange 목록 출력
    """
    return render(request, 'guide/additives/r_limejuice.html')

def rls_result(request):
    """
    r_orange 목록 출력
    """
    return render(request, 'guide/result/rlsResult.html')

def rg_result(request):
    """
    r_orange 목록 출력
    """
    return render(request, 'guide/result/rgResult.html')

def r_pineapple(request):
    """
    r_orange 목록 출력
    """
    return render(request, 'guide/additives/r_pineapple.html')

def rpc_result(request):
    """
    r_orange 목록 출력
    """
    return render(request, 'guide/result/rpcResult.html')

def gin(request):
    """
    support_vodka 목록 출력
    """
    return render(request, 'guide/support/gin.html')

def g_limejuice(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/additives/g_limejuice.html')

def gls_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/glsResult.html')

def glsp_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/glspResult.html')

def glc_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/glcResult.html')

def glt_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/gltResult.html')

def ggf_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/ggfResult.html')

def g_gingerbeer(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/additives/g_gingerbeer.html')

def ggs_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/ggsResult.html')

def whisky(request):
    """
    whisky 목록 출력
    """
    return render(request, 'guide/support/whisky.html')

def w_coffee(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/additives/w_coffee.html')

def wcw_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/wcwResult.html')

def w_sparkling(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/additives/w_sparkling.html')

def wss_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/wssResult.html')

def wc_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/wcResult.html')

def tequila(request):
    """
    whisky 목록 출력
    """
    return render(request, 'guide/support/tequila.html')

def t_orangejuice(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/additives/t_orangejuice.html')

def tog_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/togResult.html')

def t_lemonjuice(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/additives/t_lemonjuice.html')

def tlp_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/tlpResult.html')

def tls_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/tlsResult.html')

def t_limejuice(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/additives/t_limejuice.html')

def tlg_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/tlgResult.html')

def tlc_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/tlcResult.html')

def non(request):
    """
    whisky 목록 출력
    """
    return render(request, 'guide/support/non.html')

def n_lemonade(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/additives/n_lemonade.html')

def n_l_orange(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/additives/n_l_orange.html')

def nlop_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/nlopResult.html')

def n_l_eggwhite(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/additives/n_l_eggwhite.html.html')

def nles_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/nlesResult.html')

def n_grenadine(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/additives/n_grenadine.html')

def ngg_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/nggResult.html')

def ngo_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/ngoResult.html')

def n_limejuice(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/additives/n_limejuice.html')

def n_l_sparkling(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/additives/n_l_sparkling.html')

def nlss_result(request):
    """
    g_limejuice 목록 출력
    """
    return render(request, 'guide/result/nlssResult.html')