"""Pharma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views


urlpatterns = [
    path('goods_view/', views.Goods_View, name='goods_view'),
    path('goods_item_view/<int:id>/', views.Goods_Item_View, name='goods_itme_view'),
    path('goods_create/', views.Goods_Create, name='goods_create'),
    path('goods_edit/', views.Goods_Edit, name='goods_edit'),
    path('goods_delete/', views.Goods_Delete, name='goods_delete'),
    path('sales_view/', views.Sales_View, name='sales_view'),
    path('sales_create/', views.Sales_Create, name='sales_create'),
    path('sales_edit/', views.Sales_Edit, name='sales_edit'),
    path('sales_delete/', views.Sales_Delete, name='sales_delete'),
    path('sales_item_view/<int:id>/', views.Sale_Items_View, name='sales_item_view'),
    path('autocomplete_sale/', views.Autocomplete_sale, name='autocomplete_sale'),
    path('take_medicion/', views.TakeMedicion, name='take_medicion'),
    path('fill_data/', views.Filldata, name="fill_data"),

]
