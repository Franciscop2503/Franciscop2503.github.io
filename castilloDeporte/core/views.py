from msilib.schema import ListView
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from .utils import get_or_create_cart

from .models import Cart, Product

class ProductListView(ListView):
    template_name = 'Productos.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de productos'
        context['products'] = context['product_list']

        return context

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'CategoriaHombres.html'

class ProductSearchListView(ListView):
    template_name = 'search.html'

    def get_queryset(self):
        filters = Q(name__icontains=self.query()) | Q(category__name__icontains=self.query())
        return Product.objects.filter()

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['product_list'].count()

        return context


def cart(request):
    cart = get_or_create_cart(request)

    return render(request, 'cart.html', {
        'cart': cart
    })

def add(request):
    cart = get_or_create_cart(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))

    cart.add(product)

    return render(request, 'Productos.html', {
        'product' : product
    })