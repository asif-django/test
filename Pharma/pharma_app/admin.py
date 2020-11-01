from django.contrib import admin

from .models import *


# Register your models here.
admin.site.register(MyUser)
admin.site.register(MedicineName)
admin.site.register(DoctorName)


class VendorInfoAdmin(admin.ModelAdmin):
    list_display = ('id',
    'grn_type', 'received_store', 'vendor_supplier', 'invoice_no',
    'received_date', 'invoice_date', 'invoice_amount')


admin.site.register(VendorInfo, VendorInfoAdmin)


class MedicineAdmin(admin.ModelAdmin):
    list_display = ('id',
    'vendor_supplier', 'item_name', 'quantity', 'sale_quantity',
    'free_quantity', 'batch_id', 'expiry_date', 'sale_price', 'cost_price',
    'gst', 'sub_total','status','created_on')


admin.site.register(Medicine, MedicineAdmin)


class PatientInfoAdmin(admin.ModelAdmin):
    list_display = ('id',
    'store', 'bill_no', 'patient', 'referred_by', 'payment_type',
    'total_amount', 'total_vat', 'net_amount','status')


admin.site.register(PatientInfo, PatientInfoAdmin)


class PatientCollectedMedicineAdmin(admin.ModelAdmin):
    list_display = ('id',
    'patient_name', 'item_name', 'quantity', 'batch_id', 'unit_price',
    'discount', 'gst', 'sub_total','status')


admin.site.register(PatientCollectedMedicine, PatientCollectedMedicineAdmin)
