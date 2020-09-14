from django.contrib import admin
from .models import *

# Register your models here.


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('grn_type', 'received_store', 'vendor_supplier', 'invoice_no', 'received_date', 'invoice_date', 'invoice_amount' )

admin.site.register(Goods, GoodsAdmin)

class MedicineAdmin(admin.ModelAdmin):
    list_display = ('vendor_supplier', 'item_name', 'quantity', 'free_quantity', 'batch_id', 'expiry_date', 'sale_price', 'cost_price', 'gst', 'sub_total')
   
admin.site.register(Medicine, MedicineAdmin)

class SaleAdmin(admin.ModelAdmin):
    list_display = ('store', 'bill_no', 'patient', 'referred_by', 'payment_type', 'total_amount', 'total_vat', 'net_amount')

admin.site.register(Sale, SaleAdmin)

class Sale_ItemsAdmin(admin.ModelAdmin):
    list_display = ('patiant_name', 'item_name', 'quantity', 'batch_id', 'unit_price', 'discount', 'gst', 'sub_total')
admin.site.register(Sale_Items, Sale_ItemsAdmin)