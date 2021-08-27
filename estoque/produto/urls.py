from django.urls import path
from estoque.produto import views as v

app_name='produto'

urlpatterns=[
    path('', v.produto_list, name='produto_list'),
]

