import datetime

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import IntegrityError
from django.db.models import Sum
from django.forms.models import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import reverse, render, redirect, HttpResponseRedirect, \
    HttpResponse, get_object_or_404
from itertools import chain
from .filters import *
from .forms import *
from .models import *


def user_login(request):
    """
    user get authenticate
    :param request:
    :return: on successfully authenticate return to home page
    """
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email,
                            password=password)
        if user is not None:
            request.session['email'] = str(email)
            login(request, user)
            # Redirect to a success page.
            messages.success(request, 'Your login Successfully',
                             extra_tags="green")
            return redirect(reverse('home', ))
        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'incorrect username/email or password',
                           extra_tags="red")
            return HttpResponseRedirect(reverse('user_login', ))
    return render(request, 'registration/login.html')


def user_register(request):
    """
    user registration
    :param request:
    :return: on successful registration return to home page
    else registration page
    """
    if request.method == "POST":
        signup = CustSignUpForm(request.POST, request.FILES)
        if signup.is_valid():
            signup.save()
            messages.success(request, 'Your are register Successfully',
                             extra_tags='green')
            return HttpResponseRedirect(reverse('home', ))
        else:
            messages.error(request, signup.errors,
                           extra_tags='red')
            return HttpResponseRedirect(reverse('user_register', ))
    signup = CustSignUpForm()
    return render(request, 'register.html', {'signup': signup})


@login_required(login_url='/user-login/')
def user_profile(request):
    user = MyUser.objects.get(email=request.user.email)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse('home',))
        else:
            error = form.errors()
            print(error)
    context = {
        "profile_form": ProfileForm(instance=request.user),
    }
    return render(request, 'registration/profile.html', context)


@login_required(login_url='/user-login/')
def user_logout(request):
    """
    user get logout
    :param request:
    :return: after logout return login page
    """
    if request.session.has_key('email'):
        username = request.session['email']
        context = {
            'username': username,
        }
        logout(request)
        return render(request, 'registration/login.html', context)
    logout(request)
    return redirect(reverse('user_login',))


@login_required(login_url='/user-login/')
def change_password(request):
    """
    user can change old_password with new_password
    :param request:
    :return: home page
    """
    if request.method == "POST":
        old_pwd = request.POST["old_pwd"]
        new_pwd = request.POST["new_pwd"]
        cnfm_pwd = request.POST["cnfm_pwd"]

        if request.user.check_password(
                old_pwd) and new_pwd == cnfm_pwd and new_pwd != old_pwd:
            request.user.set_password(new_pwd)
            request.user.save()
        else:
            return redirect('change_password')
    return render(request, 'registration/change_password.html')


def forgot_password(request):
    """
    take email and send email with password recovery link
    :param request:
    :return:
    """
    if request.method == "POST":
        user = MyUser.objects.filter(email=request.POST.get('email'))
        if user.exists():
            url = "http://localhost:8000/set-password/" + str(
                user[0].user_uuid) + "/"
            send_mail('XYZ:Forgot password recovery', url,
                      settings.EMAIL_HOST_USER,
                      [str(user[0].email)], fail_silently=False)
            messages.success(request, 'Check your Email for Password recover', extra_tags="green")
        messages.error(request, 'Your email is no correct', extra_tags="red")
        return render(request, 'registration/forgot-password.html')
    return render(request, 'registration/forgot-password.html')


def set_password(request, uuid_id=None):
    if request.method == "POST" and uuid_id:
        new_password = request.POST["new_password"]
        cnf_password = request.POST["cnf_password"]
        if new_password == cnf_password:
            import uuid
            user = MyUser.objects.get(user_uuid=uuid_id)
            user.set_password(new_password)
            user.user_uuid = uuid.uuid4()
            user.save()
            return redirect(reverse('user_login', ))
        messages.error(request, "Password is not same", extra_tags="red")
        return render(request, 'registration/recover-password.html')
    return render(request, 'registration/recover-password.html')


@login_required(login_url='/user-login/')
def home(request):
    """
    home page
    :param request:
    :return:
    """
    return render(request, 'index.html')


@login_required(login_url='/user-login/')
def view_goods(request):
    """
    it shows all goods supply vendors info
    :param request:
    :return: goods view page
    """
    form = VendorInfo.objects.all()
    my_filter = GoodsFilter(request.GET, queryset=form)
    form = my_filter.qs
    paginator = Paginator(form, 15)
    page_no = request.GET.get('page')
    try:
        form = paginator.page(page_no)
    except PageNotAnInteger:
        form = paginator.page(1)
    except EmptyPage:
        form = paginator.page(paginator.num_pages)
    context = {
        'goods_form': form,
        'myfilter': my_filter,
    }
    return render(request, 'goods/goods_view.html', context)


@login_required(login_url='/user-login/')
def goods_item_view(request, goods_id=None):
    """
    it shows each vendor supply medicines
    :param request:
    :param goods_id:
    :return:
    """
    form = Medicine.objects.filter(vendor_supplier_id=goods_id)
    total = get_object_or_404(VendorInfo, id=goods_id)
    context = {
        'medi_form': form,
        'id': goods_id,
        'total': total.invoice_amount
    }
    return render(request, 'main.html', context)


@login_required(login_url='/user-login/')
def create_goods(request):
    """
    adding vendor info and medicines
    :param request:
    :return: goods views page
    """
    medicine_form_set = inlineformset_factory(VendorInfo, Medicine,
                                              form=MedicineForm,
                                              extra=15)
    if request.method == "POST":
        vendor_info_form = VendorInfoForm(request.POST, )
        medicine_form_set = medicine_form_set(request.POST, )
        if vendor_info_form.is_valid() and medicine_form_set.is_valid():
            v_i_f = vendor_info_form.save(commit=False)
            try:
                VendorName.objects.create(vendor_name=v_i_f.vendor_supplier)
            except IntegrityError:
                pass
            m_f = medicine_form_set.save(commit=False)
            for f in m_f:
                if f.item_name:
                    try:
                        MedicineName.objects.create(medicines=f.item_name)
                    except IntegrityError:
                        pass
                    f.vendor_supplier = v_i_f
                    f.sale_quantity = int(f.quantity)+int(f.free_quantity)
                    v_i_f.save()
                    f.save()
            messages.success(request, 'Data added successfully',
                             extra_tags='green')
            return redirect('/goods_view/')

        else:
            messages.error(request, 'Data adding failed!', extra_tags='red')
            return redirect('/goods_create')

    context = {
        'goods_form': VendorInfoForm(),
        'medi_form': medicine_form_set(),

    }
    return render(request, 'goods/goods_create.html', context)


class DoesNotExist(object):
    pass


@login_required(login_url='/user-login/')
def edit_goods(request, goods_id):
    """
    Edit vendor info and it's medicines
    :param request:
    :param goods_id:
    :return:
    """
    ven_info = VendorInfo.objects.get(id=goods_id)
    medicine_form_set = inlineformset_factory(VendorInfo, Medicine,
                                              form=MedicineForm,
                                              extra=2)
    vend_form = VendorInfoForm(instance=ven_info)
    medicine_form = medicine_form_set(instance=ven_info)
    if request.method == 'POST':
        update_vendor_form = VendorInfoForm(request.POST, instance=ven_info)
        update_medicine_form_set = medicine_form_set(request.POST,
                                                     instance=ven_info)

        if update_medicine_form_set.is_valid() and update_vendor_form.is_valid():
            u_v_f = update_vendor_form.save(commit=False)
            u_m_f = update_medicine_form_set.save(commit=False)
            for form in u_m_f:
                if form.item_name:
                    form.vendor_supplier = u_v_f
                    u_v_f.save()
                    form.save()

            messages.success(request,
                             'Your are Data Updated Successfully',
                             extra_tags='green')
    context = {
        "goods_form": vend_form,
        "medi_form": medicine_form,
        "patient_id": goods_id
    }
    return render(request, 'goods/goods_edit.html', context)


@login_required(login_url='/user-login/')
def delete_goods(request, del_id):
    """
    Delete vendor info and medicine
    :param request:
    :param del_id:
    :return:
    """
    try:
        vendor_data = VendorInfo.objects.get(id=del_id)
        medicine = Medicine.objects.filter(vendor_supplier_id=del_id)
    except VendorInfo.DoesNotExist:
        messages.error(request, 'Data not deleted',
                       extra_tags="red")
        return redirect(reverse('goods_view', ))
    else:
        vendor_data.delete()
        medicine.delete()
    messages.success(request, 'Data deleted successfully', extra_tags='green')
    return redirect(reverse('goods_view', ))


@login_required(login_url='/user-login/')
def view_sale(request):
    """
    show all patient info
    :param request:
    :return:
    """
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    form = PatientInfo.objects.all().order_by("-id")
    total = PatientInfo.objects.aggregate(Sum('total_amount'))
    today_sale = PatientInfo.objects.filter(sale_date=today).aggregate(
        Sum('total_amount'))
    yesterday_sale = PatientInfo.objects.filter(sale_date=yesterday).aggregate(
        Sum('total_amount'))
    cash = PatientInfo.objects.filter(payment_type="Cash").aggregate(
        Sum('total_amount'))
    card = PatientInfo.objects.filter(payment_type="Card").aggregate(
        Sum('total_amount'))
    upi = PatientInfo.objects.filter(payment_type="UPI").aggregate(
        Sum('total_amount'))
    others = PatientInfo.objects.filter(payment_type="Others").aggregate(
        Sum('total_amount'))
    myfilter = SaleFilter(request.GET, queryset=form)
    form = myfilter.qs
    paginator = Paginator(form, 15)
    page_no = request.GET.get('page')
    try:
        form = paginator.page(page_no)
    except PageNotAnInteger:
        form = paginator.page(1)
    except EmptyPage:
        form = paginator.page(paginator.num_pages)
    context = {
        'sale_form': form,
        'bills': PatientInfo.objects.count(),
        'total': total['total_amount__sum'],
        'cash': cash['total_amount__sum'],
        'card': card['total_amount__sum'],
        'upi': upi['total_amount__sum'],
        'others': others['total_amount__sum'],
        'today_sale': today_sale['total_amount__sum'],
        'yesterday_sale': yesterday_sale['total_amount__sum'],
        'myfilter': myfilter,

    }
    return render(request, 'sales/sales_view.html', context)


@login_required(login_url='/user-login/')
def sale_items_view(request, patient_id):
    """
    show each patient collected medicine
    :param request:
    :param patient_id:
    :return:
    """
    form = PatientCollectedMedicine.objects.filter(patient_name_id=patient_id)
    total = PatientInfo.objects.get(id=patient_id)
    context = {
        'sale_item_form': form,
        'id': patient_id,
        'total': total.total_amount,
    }
    return render(request, 'main.html', context)


@login_required(login_url='/user-login/')
def create_sale(request):
    """
    add patient info along with medicine
    :param request:
    :return: same page with message
    """
    patient_collected_medicine_formset = inlineformset_factory(PatientInfo,
                                                               PatientCollectedMedicine,
                                                               form=PatientCollectedMedicineForm,
                                                               extra=10)
    if request.method == "POST":
        sale_form = PatientInfoForm(request.POST)
        sale_item_form = patient_collected_medicine_formset(request.POST)
        if sale_form.is_valid() and sale_item_form.is_valid():
            sf = sale_form.save(commit=False)
            sf.save()
            if sf.bill_no is None and sf.id:
                sf.bill_no = "DSRBIL" + str(sf.id)
                sf.save()
            mf = sale_item_form.save(commit=False)
            for f in mf:
                if f.item_name:
                    fq = f.quantity
                    b_id = f.batch_id
                    fn = f.item_name
                    data = Medicine.objects.filter(item_name__iexact=fn,
                                                   batch_id=b_id)
                    # We are taking available medicine quantity and
                    # subtracting with patient purchase quantity.
                    available_quantity = data[
                        0].sale_quantity
                    # that particular field value.
                    update_quantity = available_quantity - int(fq)
                    data.update(
                        sale_quantity=update_quantity)
                    # update that particular field with new value
                    f.patient_name = sf
                    f.save()
                    url = "/print/" + str(sf.id) + "/"
                    # To show print popup we are sending this url.
            messages.success(request,
                             'Your are Data Updated Successfully',
                             extra_tags='green')
            context = {
                'sale_form': PatientInfoForm(),
                'sale_item_form': patient_collected_medicine_formset(),
                "url": url

            }
            return render(request, 'sales/sales_create.html', context)

        else:
            messages.error(request, 'Data adding failed!', extra_tags='red')
            return redirect('/sales_create')

    context = {
        'sale_form': PatientInfoForm(),
        'sale_item_form': patient_collected_medicine_formset(),
    }
    return render(request, 'sales/sales_create.html', context)


@login_required(login_url='/user-login/')
def edit_sale(request, patient_id):
    """
    Exchange/Return sold medicine and add new medicine
    :param request:
    :param patient_id:
    :return:
    """
    print(patient_id)
    patient_data = PatientInfo.objects.get(id=patient_id)
    patient_collected_medicine_formset = inlineformset_factory(PatientInfo,
                                                               PatientCollectedMedicine,
                                                               form=PatientCollectedMedicineForm,
                                                               max_num=1)
    if request.method == "POST":
        patient_data_form = PatientInfoForm(request.POST,
                                            instance=patient_data)
        formset = patient_collected_medicine_formset(request.POST,
                                                     instance=patient_data)
        if formset.is_valid() and patient_data_form.is_valid():
            patient_from = patient_data_form.save(commit=False)
            pdf = formset.save(commit=False)
            for f in pdf:
                if f.item_name and f.id:
                    # Previous quantity.
                    patient_available_quantity = get_object_or_404(
                        PatientCollectedMedicine, id=f.id).quantity
                    # Get particular medicine to update it's sale_quantity.
                    medicine_update = Medicine.objects.filter(
                        item_name=f.item_name, batch_id=f.batch_id)
                    # Get available particular medicine sale_quantity in store.
                    medicine_quantity = medicine_update[0].sale_quantity
                    if int(f.quantity) < int(patient_available_quantity):
                        update_with = int(patient_available_quantity) - int(
                            f.quantity)
                        update_quantity = medicine_quantity + update_with
                        medicine_update.update(
                            sale_quantity=update_quantity)
                        # update that particular field with new value
                        f.patient_name = patient_from
                        patient_from.save()
                        f.save()
                    elif int(f.quantity) > int(patient_available_quantity):
                        update_with = int(f.quantity) - int(
                            patient_available_quantity)
                        update_quantity = medicine_quantity - update_with
                        medicine_update.update(
                            sale_quantity=update_quantity)
                        # update that particular field with new value
                        f.patient_name = patient_from
                        patient_from.save()
                        f.save()
                    else:
                        f.patient_name = patient_from
                        patient_from.save()
                        f.save()
                elif f.item_name and f.id is None:
                    medicine_update = Medicine.objects.filter(
                        item_name=f.item_name, batch_id=f.batch_id)
                    update_quantity = medicine_update[
                                          0].sale_quantity - int(
                        f.quantity)
                    medicine_update.update(
                        sale_quantity=update_quantity)
                    f.patient_name = patient_from
                    patient_from.save()
                    f.save()
                else:
                    try:
                        data = PatientCollectedMedicine.objects.get(id=f.id)
                    except PatientCollectedMedicine.DoesNotExist:
                        pass
                    else:
                        medicine_update = Medicine.objects.filter(
                            item_name=data.item_name, batch_id=data.batch_id)
                        update_quantity = medicine_update[
                                              0].sale_quantity + int(
                            data.quantity)
                        medicine_update.update(
                            sale_quantity=update_quantity)
                        data.delete()
            messages.success(request,
                             'Your are Data Updated Successfully',
                             extra_tags='green')
        else:
            p = formset.errors
            print("Errors ", p)
    patient_data_form = PatientInfoForm(instance=patient_data)
    medicine_collect_form = patient_collected_medicine_formset(
        instance=patient_data)
    context = {
        "patient_data_form": patient_data_form,
        "medicine_collect_form": medicine_collect_form,
        "patient_id": patient_id
    }
    return render(request, 'sales/sales_edit.html', context)


@login_required(login_url='/user-login/')
def delete_sales(request, del_id=None):
    """
    delete patient info and his collected medicine
    :param request:
    :param del_id:
    :return:
    """
    try:
        patient_data = PatientInfo.objects.get(id=del_id)
        patient_collect_data = PatientCollectedMedicine.objects.filter(
            patient_name_id=del_id)
    except PatientInfo.DoesNotExist:
        messages.error(request, 'Data not deleted',
                       extra_tags='red')
        return redirect(reverse('sales_view', ))
    else:
        patient_data.delete()
        patient_collect_data.delete()
    messages.success(request, 'Data deleted successfully', extra_tags='green')
    return redirect(reverse('sales_view', ))


@login_required(login_url='/user-login/')
def fill_data(request):
    """
    get medicine name and return the all remaining medicine details.
    :param user_id:
    :param request:
    :param value: tablate name
    :return: return in json format
    """
    data = Medicine.objects.filter(item_name__iexact=request.GET['value'])
    xyz = PatientCollectedMedicine.objects.filter(id=request.GET['user_id'])
    combined = list(chain(data, xyz))
    v = serializers.serialize('json', combined)
    return HttpResponse(v, content_type="application/json")


@login_required(login_url='/user-login/')
def print_bill(request, id=None):
    """
    print the bill
    :param request:
    :param id:
    :return:
    """
    patient_collect_item = PatientCollectedMedicine.objects.filter(
        patient_name_id=id)
    patient_info = PatientInfo.objects.get(id=id)
    context = {
        'sale_form': patient_info,
        'sale_item': patient_collect_item,
    }
    return render(request, 'print.html', context)


@login_required(login_url='/user-login/')
def tablet_name(request):
    """
    this get the medicine for dropdown
    :param request:
    :return:
    """
    if 'term' in request.GET:
        qs = MedicineName.objects.filter(
            medicines__istartswith=request.GET.get('term'),
        )[:3]
        titles = list()
        for product in qs:
            titles.append(product.medicines)
        # titles = [product.title for product in qs]
        return JsonResponse(titles, safe=False)
    # return render(request, 'core/home.html')


@login_required(login_url='/user-login/')
def vendor_list(request):
    """
    vendor name autocomplete
    :param request:
    :return:
    """
    if 'term' in request.GET:
        qs = VendorName.objects.filter(
            vendor_name__istartswith=request.GET.get('term'), )[:3]
        vendor_name = list()
        for product in qs:
            vendor_name.append(product.vendor_name)
        return JsonResponse(vendor_name, safe=False)


@login_required(login_url='/user-login/')
def invoice_list(request):
    """
    get all invoices as dropdown
    :param request:
    :return:
    """
    if "term" in request.GET:
        qs = VendorInfo.objects.filter(invoice_no__istartswith=request.GET.get('term'),)[:3]
        vendor_name = list()
        for product in qs:
            vendor_name.append(product.invoice_no)
        return JsonResponse(vendor_name, safe=False)


@login_required(login_url='/user-login/')
def bill_no(request):
    """
    get all bill no. as dropdown
    :param request:
    :return:
    """
    if "term" in request.GET:
        qs = PatientInfo.objects.filter(bill_no__istartswith=request.GET.get('term'),)[:3]
        vendor_name = list()
        for product in qs:
            vendor_name.append(product.bill_no)
        return JsonResponse(vendor_name, safe=False)


@login_required(login_url='/user-login/')
def patient_phone(request):
    """
    get all bill no. as dropdown
    :param request:
    :return:
    """
    if "term" in request.GET:
        qs = PatientInfo.objects.filter(phone__istartswith=request.GET.get('term'),)[:3]
        vendor_name = list()
        for product in qs:
            vendor_name.append(product.phone)
        return JsonResponse(vendor_name, safe=False)