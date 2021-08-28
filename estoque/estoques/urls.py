from django.urls import path
from estoque.estoques import views as v

app_name = 'estoques'

urlpatterns=[
    path('', v.estoque_entrada_list, name='estoque_entrada_list'),
]