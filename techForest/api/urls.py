from django.urls import path

from . import views

urlpatterns = [
    path('usuario',views.usuario_list),
    path('usuario/<int:pk>',views.usuario_detail),
    path('planes',views.planes_list),
    path('planes/<int:pk>',views.planes_detail),
    path('pagos',views.pagos_list),
    path('pagos/<int:pk>',views.pagos_detail),
    path('error',views.error_list),
    path('error/<int:pk>',views.error_detail),
    path('diapositivos',views.diapositivos_list),
    path('diapositivos/<int:pk>',views.diapositivos_detail),
    path('valvula',views.valvula_list),
    path('valvula/<int:pk>',views.valvula_detail),
    path('valvula/diapositivos/<int:pk>',views.valvula_diapositivos_detail),
    path('opciones',views.opciones_list),
    path('opciones/<int:pk>',views.opciones_detail),
    path('admin',views.admin_list),
    path('admin/<int:pk>',views.admin_detail)
]