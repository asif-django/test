import django_filters
from .models import *
from tempus_dominus.widgets import DatePicker

class SaleFilter(django_filters.FilterSet):
    From = django_filters.DateFilter(field_name="created_on", lookup_expr="gte", label='From')
    To = django_filters.DateFilter(field_name="created_on", lookup_expr="lte", label='To')

    
    class Meta:
        model = Sale
        fields = ['bill_no', 'phone']
    


class GoodsFilter(django_filters.FilterSet):
    From = django_filters.DateFilter(field_name="created_on", lookup_expr="gte", label='From')
    To = django_filters.DateFilter(field_name="created_on", lookup_expr="lte", label='To')

    class Meta:
        model = Goods
        fields = ['vendor_supplier', 'invoice_no', 'received_store', 'grn_type']
        