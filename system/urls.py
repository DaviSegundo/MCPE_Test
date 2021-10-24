from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:processo_cod>', views.processos, name='processos'),
    path('criar_p', views.criar, name='criar'),
    path('buscar', views.buscar, name='buscar'),
    path('editar/<int:processo_cod>', views.editar, name='editar'),
    path('excluir/<int:processo_cod>', views.excluir, name='excluir')
]