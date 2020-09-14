from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from tempus_dominus.widgets import DatePicker

class GoodsForm(ModelForm):
    class Meta:
        model = Goods
        fields = '__all__'
        widgets = {
        'received_date': DatePicker(),
        'invoice_date' : DatePicker(),

        }
        #exclude = ['gst_amount', 'remarks', 'net_amount', 'round_off']



class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        exclude = ['vendor_supplier',]
        widgets = {
        'expiry_date': DatePicker(),

        }


class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'data-inputmask': '"mask": "999-999-9999"'})
        

class Sale_ItemsForm(ModelForm):
    class Meta:
        model = Sale_Items
        exclude = ['patiant_name']