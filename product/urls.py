from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductLV.as_view(), name='index'),
    path('product/<int:pk>/', views.ProductDV.as_view(), name='product_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)