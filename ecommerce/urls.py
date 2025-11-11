"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views as main_view
from product_app import views as p_view

urlpatterns = [
    path('', include('ecomm_core.urls')),
    path('admin/', admin.site.urls),
    path('home/', main_view.home_pg , name='home'),
    path('about/', main_view.about_pg , name='about'),
    path('contact/', main_view.contact_pg , name='contact'),
    path('login/', main_view.login_pg , name='login'),
    path('regist/', main_view.register_pg , name='register'),
    path('plistviewfvb/', p_view.product_list_view , name='productlistview'),
    path('plistviewcvb/', p_view.ProductListView.as_view() , name='classbaseproductlistview'),
    path('pdetailviewfvb/<int:id>/',p_view.product_detail_view, name='productdetailview'),
    path('pdetailviewcvb/<int:id>/', p_view.ProductDetailView.as_view(), name='classbaseproductdetailview'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)