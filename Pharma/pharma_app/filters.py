import django_filters
from tempus_dominus.widgets import DatePicker

from .models import *


class SaleFilter(django_filters.FilterSet):
    From = django_filters.DateFilter(field_name="sale_date", lookup_expr="gte",
                                     label='From', widget=DatePicker())
    To = django_filters.DateFilter(field_name="sale_date", lookup_expr="lte",
                                   label='To', widget=DatePicker())

    class Meta:
        model = PatientInfo
        fields = ['bill_no', 'phone']


class GoodsFilter(django_filters.FilterSet):
    received_date = django_filters.DateFilter(field_name="received_date",
                                              lookup_expr="gte",
                                              label='Received_date',
                                              widget=DatePicker())
    invoice_date = django_filters.DateFilter(field_name="invoice_date",
                                             lookup_expr="lte",
                                             label='Invoice_date',
                                             widget=DatePicker())

    class Meta:
        model = VendorInfo
        fields = ['vendor_supplier', 'invoice_no', 'received_store',
                  'received_date', 'invoice_date']
