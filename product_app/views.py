from django.shortcuts import render , get_object_or_404 , Http404
from django.views.generic import ListView , DetailView
from .models import Product

# Create your views here.

'''
this is class based view  which is list view  
'''
class ProductListView(ListView):
    queryset = Product.objects.all()
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

'''
here are the detail view 
'''

class ProductDetailView(ListView):
    queryset = Product.objects.all()
    template_name = "product/product_detail_view.html"


    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView,self).get_context_data(*args,**kwargs)
        print(context)
        return context



def product_detail_view(request,id):
    # queryset = Product.objects.all()
    # instance = get_object_or_404(Product,id=id)
    # try:
    #     instace = get_object_or_404(Product,id=id)
    # except Product.DoesNotExist:
    #     print("No product here")
    # except:
    #     print("product_id",id)
    # context = {
    #     "object_list" : instance
    # }

    qs = Product.objects.filter(id=id)
    if qs.exists() :
        instace = qs.first()
    else:
        raise Http404("product not found")

    return render(request, "product/product_detail_view.html", context)

