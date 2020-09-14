from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, get_list_or_404, get_object_or_404
from .models import *
from .forms import *
from django.db import IntegrityError
from django.contrib import messages
from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms.models import modelformset_factory, inlineformset_factory
from django.db.models import Sum
from django.core import serializers
from django.http import JsonResponse
from .filters import *

# Create your views here.



def Goods_View(request):
    form = Goods.objects.all()
    myFilter = GoodsFilter(request.GET, queryset=form)
    form = myFilter.qs
    context = {
        'goods_form':form,
        'myfilter' : myFilter,
    }
    return render(request, 'goods/goods_view.html', context)

def Goods_Item_View(request, id=None):
    form = Medicine.objects.filter(vendor_supplier_id=id)
    context = {
    'medi_form':form,
    }
    return render(request, 'main.html', context)


def Goods_Create(request):
    medi_form = inlineformset_factory(Goods, Medicine, form=MedicineForm, extra=15)
    if request.method=="POST":
        goods_form = GoodsForm(request.POST,)
        medi_form = medi_form(request.POST,)
        if goods_form.is_valid() and medi_form.is_valid():
            gf = goods_form.save(commit=False)
            gf.save()
            mf = medi_form.save(commit=False)
            for f in mf:
                if f.item_name:
                    f.vendor_supplier = gf
                    f.save()

            messages.success(request, 'Data added successfully', extra_tags='green')
            return redirect('/goods_view')

        else:
            messages.error(request, 'Data adding failed!', extra_tags='red')
            return redirect('/goods_create')



    context = {
        'goods_form':GoodsForm(),
        'medi_form':medi_form(),

    }
    return render(request, 'goods/goods_create.html', context)

def Goods_Edit(request):
    return render(request, 'main.html')

def Goods_Delete(request):
    return render(request, 'index.html')


def Sales_View(request):
    form = Sale.objects.all()
    total = Sale.objects.aggregate(Sum('total_amount'))
    cash = Sale.objects.filter(payment_type="Cash").aggregate(Sum('total_amount'))
    card = Sale.objects.filter(payment_type="Card").aggregate(Sum('total_amount'))
    upi = Sale.objects.filter(payment_type="UPI").aggregate(Sum('total_amount'))
    others = Sale.objects.filter(payment_type="Others").aggregate(Sum('total_amount'))
    myFilter = SaleFilter(request.GET, queryset=form)
    form = myFilter.qs
    context = {
        'sale_form' : form,
        'bills' : form.count(),
        'total' : total['total_amount__sum'],
        'cash' : cash['total_amount__sum'],
        'card' : card['total_amount__sum'], 
        'upi' : upi['total_amount__sum'],
        'others' : others['total_amount__sum'],
        'myfilter' : myFilter

    }
    return render(request, 'sales/sales_view.html', context)


def Sale_Items_View(request, id=None):
    form = Sale_Items.objects.filter(patiant_name_id=id)
    # serialized_qs = serializers.serialize('json', form)
    # data = {"queryset" : serialized_qs}
    # return JsonResponse(data)
    context = {
    'sale_item_form':form,
    }
    return render(request, 'main.html', context)

def Sales_Create(request):
    sale_items = inlineformset_factory(Sale, Sale_Items, form=Sale_ItemsForm, extra=10)
    if request.method=="POST":
        sale_form = SaleForm(request.POST,)
        sale_item_form = sale_items(request.POST,)
        if sale_form.is_valid() and sale_item_form.is_valid():
            sf = sale_form.save(commit=False)
            sf.save()
            mf = sale_item_form.save(commit=False)
            for f in mf:
                if f.item_name:
                    f.patiant_name = sf
                    f.save()

            messages.success(request, 'Data added successfully', extra_tags='green')
            return redirect('/sales_view')

        else:
            messages.error(request, 'Data adding failed!', extra_tags='red')
            return redirect('/goods_create')



    context = {
        'sale_form':SaleForm(),
        'sale_item_form':sale_items(),

    }
    return render(request, 'sales/sales_create.html', context)

def Sales_Edit(request):
    pass

def Sales_Delete(request):
    pass

def Autocomplete_sale(request):
    if 'term' in request.GET:
        sale = Medicine.objects.filter(item_name__icontains=request.GET.get("term"))
        l = list()
        for x in sale:
            l.append(x.item_name)
        return JsonResponse(l, safe=False)


def TakeMedicion(request):
    data = Medicine.objects.values("item_name")
    print(data)
    print("%$"*20)    
    l = list()
    for x in data:
        l.append(x['item_name']+',')
    print("l values: ",l)
    return HttpResponse(l)
    
def Filldata(request):
    data = Medicine.objects.filter(item_name__icontains="para")
    v = serializers.serialize('json', data)
    print(v)
    print("#"*20)
    return HttpResponse(v, content_type="application/json")



