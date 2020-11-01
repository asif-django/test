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
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # All goods URLS.
    path('goods_view/', views.view_goods, name='goods_view'),
    path('goods_item_view/<int:goods_id>/', views.goods_item_view,
         name='goods_item_view'),
    path('goods_create/', views.create_goods, name='goods_create'),
    path('goods_edit/<int:goods_id>/', views.edit_goods, name='goods_edit'),
    path('goods_delete/<int:del_id>/', views.delete_goods,
         name='goods_delete'),

    # All sales URLS.
    path('sales_view/', views.view_sale, name='sales_view'),
    path('sales_item_view/<int:patient_id>/', views.sale_items_view,
         name='sales_item_view'),
    path('sales_create/', views.create_sale, name='sales_create'),
    path('sales_edit/<int:patient_id>/', views.edit_sale, name='sales_edit'),
    path('sales_delete/<int:del_id>/', views.delete_sales,
         name='sales_delete'),

    # All Authentication urls.
    path('user-login/', views.user_login, name='user_login'),
    path('user-logout/', views.user_logout, name='user_logout'),
    path('user-register/', views.user_register, name='user_register'),
    path('change-user-password/', views.change_password,
         name='user_password_change'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('set-password/<str:uuid_id>/', views.set_password, name="set_password"),
    path('user-profile', views.user_profile, name="user_profile"),

    # Extra urls.
    path('medicine-auto/', views.tablet_name, name='tablet_name'),
    path('vendor-list/', views.vendor_list, name="vendor_list"),
    path('invoice-list/', views.invoice_list, name="invoice_list"),
    path('bill-no/', views.bill_no, name="bill_no"),
    path('patient-phone/', views.patient_phone, name="patient_phone"),
    path('fill_data/', views.fill_data, name="fill_data"),
    path('print/<int:id>/', views.print_bill, name="print"),

]
