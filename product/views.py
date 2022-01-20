from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.views.generic import ListView, DetailView

from .models import Product
# Create your views here.

class ProductLV(ListView):
    model = Product

class ProductDV(DetailView):
    model = Product

# def all_products_by_category(request, category_slug=None):
#     category_page = None
#     products_list = None
#
#     if category_slug is not None:
#         category_page = get_object_or_404(Category, slug=category_slug)
#         products_list = Product.objects.filter(
#             category=category_page,
#             available=True,
#         )
#     else:
#         products_list = Product.objects.all().filter(available=True)
#
#     paginator = Paginator(products_list, 6)
#     try:
#         page = int(request.GET.get('page', '1'))
#     except:
#         page = 1
#
#     try:
#         products = paginator.page(page)
#     except (EmptyPage, InvalidPage):
#         products = paginator.page(paginator.num_pages)
#
#     context = {
#         'category': category_page,
#         'products': products,
#     }
#     return render(request, 'homepage.html', context)
