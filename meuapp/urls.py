from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar, name='listar'),
    path('adicionar_cliente/', views.adicionar_cliente, name='adicionar_cliente'),
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto'),
    path('editar_cliente/<str:cpf>/', views.editar_cliente, name='editar_cliente'),
    path('editar_produto/<int:id>/', views.editar_produto, name='editar_produto'),
    path('deletar_cliente/<str:cpf>/', views.deletar_cliente, name='deletar_cliente'),
    path('deletar_produto/<int:id>/', views.deletar_produto, name='deletar_produto'),
]
