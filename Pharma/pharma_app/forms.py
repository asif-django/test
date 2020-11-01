from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, forms
from tempus_dominus.widgets import DatePicker

from .models import *


class VendorInfoForm(ModelForm):
    class Meta:
        model = VendorInfo
        fields = '__all__'
        widgets = {
            'received_date': DatePicker(),
            'invoice_date': DatePicker(),

        }
        # exclude = ['gst_amount', 'remarks', 'net_amount', 'round_off']


class GoodsFilterForm(ModelForm):
    class Meta:
        model = VendorInfo
        fields = ['vendor_supplier', 'invoice_no', 'grn_type', 'received_date',
                  'invoice_date']
        widgets = {
            'received_date': DatePicker(),
            'invoice_date': DatePicker(),
        }


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        exclude = ['vendor_supplier', ]
        widgets = {
            'expiry_date': DatePicker(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gst'].widget.attrs.update(
            {"onchange": "getMedTotal(this)"})
        self.fields['quantity'].widget.attrs.update(
            {"onchange": "getMedTotal(this)"})


class PatientInfoForm(ModelForm):
    class Meta:
        model = PatientInfo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update(
            {'data-inputmask': '"mask": "999-999-9999"'})


class PatientCollectedMedicineForm(ModelForm):
    class Meta:
        model = PatientCollectedMedicine
        exclude = ['patient_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item_name'].widget.attrs.update(
            {"onchange": "getFieldValues(this)"})
        self.fields['quantity'].widget.attrs.update(
            {"onchange": "getSumOf(this)"})


class CustSignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['user_name', 'email', 'date_of_birth', 'mobile', 'photo']
        widgets = {
            'date_of_birth': DatePicker(),
        }


class ProfileForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['user_name', 'email', 'date_of_birth', 'mobile', 'photo']
        widgets = {
            'date_of_birth': DatePicker(),
        }

