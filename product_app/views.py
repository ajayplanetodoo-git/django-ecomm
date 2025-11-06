from django.shortcuts import render 
from django.views.generic.list import ListView
from .models import Product

# Create your views here.
class ProductListView(ListView):
    product_queryset = Product.objects.all()
    template_name = "product/product_list_view.html"


    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView,self).get_context_data(*args,**kwargs)

        return context



def product_list_view(request):
    queryset = Product.objects.all()

    context = {
        "object_list" : queryset
    }
    return render(request, "product/product_list_view.html", context)