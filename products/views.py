
from django.views import generic

from products.models import Product


class ProductListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    context_object_name = 'products'
    template_name = 'products/product_list.html'


class ProductDetailView(generic.DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'

