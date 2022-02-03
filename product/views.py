from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.views.generic import ListView, DetailView

from .models import Product
# Create your views here.

class ProductLV(ListView):
    model = Product

class ProductDV(DetailView):
    model = Product

