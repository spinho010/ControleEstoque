from django.shortcuts import render
from .models import Produto
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import ProdutoForm
from django.urls import reverse_lazy


def produto_list(request):
    template_name = 'produto_list.html'
    objects=Produto.objects.all()
    context={'object_list': objects}
    return render(request, template_name, context)


def produto_detail(request, pk):
    template_name = 'produto_detail.html'
    obj=Produto.objects.get(pk=pk)
    context={'object': obj}
    return render(request, template_name, context)


def produto_add(request):
    template_name = 'produto_form.html'
    return render(request, template_name)


class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm
    success_url = ('/')
    
