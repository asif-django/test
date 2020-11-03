import uuid

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models

# Create your models here.


GRN_TYPES = (('A', 'A'), ('B', 'B'), ('C', 'C'))

NAMES = (('D. Sujatha', 'D. Sujatha'), ('D. Shantha Rao', 'D. Shantha Rao'))

PYMENT_TYPE = (('Cash', 'Cash'), ('Card', 'Card'), ('UPI', 'UPI'),
               ('Others', 'Others'))

QUANTITY = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"))

GST = (("5", "5%"), ("12", "12%"), ("18", "18%"))

SEX = (("MALE", "MALE"), ("FEMALE", "FEMALE"))


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    """
    creating user by inheriting AbstractBaseUser
    """
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False,
                                 verbose_name="user uuid")
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    user_name = models.CharField(max_length=255, verbose_name="User Name",
                                 null=True,
                                 blank=True)
    mobile = models.CharField(max_length=255, blank=True,
                              verbose_name="Mobile Number",
                              null=True)
    photo = models.ImageField(upload_to='user/images', blank=True,
                              verbose_name="Image", null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class DoctorName(models.Model):
    doctor_name = models.CharField(max_length=100, null=True, blank=True,
                                   verbose_name="Doctor Name")
    doctor_age = models.CharField(max_length=100, null=True, blank=True,
                                  verbose_name="Age")
    sex = models.CharField(max_length=10, choices=SEX, default="FEMALE",
                                  verbose_name="Sex")
    email = models.EmailField(null=True, blank=True,
                                     verbose_name="Email")
    phone = models.CharField(max_length=100, null=True, blank=True,
                                    verbose_name="Phone")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.doctor_name)


class VendorInfo(models.Model):
    '''
    here we are collecting vendor_supplier info
    '''
    grn_type = models.CharField(max_length=50, null=True, blank=True,
                                default="Purchase Received", verbose_name="GRN_Type")
    received_store = models.CharField(max_length=50, null=True, blank=True,
                                      default="Ramnagar",
                                      verbose_name="Received Store")
    vendor_supplier = models.CharField(max_length=50, null=True, blank=True,
                                       verbose_name="Vendor/Supplier")
    invoice_no = models.CharField(max_length=100, null=True, blank=True,
                                  verbose_name="D/C or Invoice No")
    received_date = models.DateField(null=True, blank=True,
                                     verbose_name="Received Date")
    received_by = models.CharField(max_length=50, blank=True, null=True,
                                   choices=NAMES, default="D. Sujatha",
                                   verbose_name="Received By")
    invoice_date = models.DateField(null=True, blank=True,
                                    verbose_name="Invoice Date")
    invoice_amount = models.FloatField(null=True, blank=True,
                                       verbose_name="Invoice Amount")
    gst_amount = models.FloatField(null=True, blank=True,
                                   verbose_name="GST Amount")
    remarks = models.CharField(max_length=150, null=True, blank=True,
                               verbose_name="Remarks")
    net_amount = models.FloatField(null=True, blank=True,
                                   verbose_name="Net_Amount")
    round_off = models.IntegerField(null=True, blank=True,
                                    verbose_name="Round Off")

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.vendor_supplier)


class Medicine(models.Model):
    """
    here we collecting that particular vendor supplied medicine
    with expiry date, price, gst and quantity
    """
    vendor_supplier = models.ForeignKey(VendorInfo, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50, null=True, blank=True,
                                 verbose_name="Item Name")
    quantity = models.IntegerField(default=0, blank=True,
                                   verbose_name="Quantity")
    sale_quantity = models.IntegerField(default=0, blank=True,
                                        verbose_name="Sale Quantity")
    free_quantity = models.IntegerField(default=0, blank=True,
                                        verbose_name="Free Quantity")
    batch_id = models.CharField(max_length=50, null=True, blank=True,
                                verbose_name="Batch ID")
    expiry_date = models.DateField(null=True, blank=True,
                                   verbose_name="Expiry Date")
    sale_price = models.FloatField(null=True, blank=True,
                                   verbose_name="Sale Price")
    cost_price = models.FloatField(null=True, blank=True,
                                   verbose_name="Cost Price")
    gst = models.CharField(max_length=50, null=True, blank=True, choices=GST,
                           verbose_name="GST(%)")
    sub_total = models.FloatField(null=True, blank=True,
                                  verbose_name="Sub Total")

    is_active = models.BooleanField(default=True,)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return str(self.vendor_supplier)


class PatientInfo(models.Model):
    """
    here collecting patient info with referred doctor name and total bill
    """
    DoesNotExist = None
    objects = None
    store = models.CharField(max_length=50, null=True, blank=True,
                             default="Ramnagar", verbose_name="Store")
    bill_no = models.CharField(max_length=50, null=True, blank=True,
                               verbose_name="Bill_No")
    patient = models.CharField(max_length=50, null=True, blank=True,
                               verbose_name="Patien Name")
    phone = models.CharField(max_length=50, null=True, blank=True,
                             verbose_name="Mobile Number")
    referred_by = models.ForeignKey(DoctorName, on_delete=models.SET_NULL,
                                    null=True, default='',
                                    verbose_name="Referred By")
    payment_type = models.CharField(max_length=50, null=True, blank=True,
                                    choices=PYMENT_TYPE,
                                    verbose_name="Payment Type")
    total_vat = models.FloatField(null=True, blank=True,
                                  verbose_name="GST Amount")
    net_amount = models.FloatField(null=True, blank=True,
                                   verbose_name="Net_Amount")
    total_amount = models.FloatField(null=True, blank=True,
                                     verbose_name="Total_Amountt")
    sale_date = models.DateField(auto_now_add=True, null=True)

    is_active = models.BooleanField(default=True,)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.patient)


class PatientCollectedMedicine(models.Model):
    """
    here we are collecting that particular patient taken medicine info
    """
    DoesNotExist = None
    objects = None
    patient_name = models.ForeignKey(PatientInfo, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50, null=True, blank=True,
                                 verbose_name="Item Name")
    quantity = models.CharField(max_length=10, null=True, blank=True,
                                verbose_name="Quantity")
    batch_id = models.CharField(max_length=50, null=True, blank=True,
                                verbose_name="Batch ID")
    unit_price = models.FloatField(null=True, blank=True,
                                   verbose_name="Unit Price")
    expiry_date = models.DateField(null=True, blank=True,
                                   verbose_name="Expiry Date")
    discount = models.FloatField(null=True, blank=True,
                                 verbose_name="Discount")
    gst = models.FloatField(null=True, blank=True, verbose_name="GST(%)")
    sub_total = models.FloatField(null=True, blank=True,
                                  verbose_name="Sub Total")

    is_active = models.BooleanField(default=True,)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.item_name)


class MedicineName(models.Model):
    """
    store medicines
    """
    objects = None
    medicines = models.CharField(max_length=100, null=True, blank=True,
                                 unique=True, verbose_name="Medicine Name")

    def __str__(self):
        return str(self.medicines)


class VendorName(models.Model):
    """
    add vendor names
    """
    vendor_name = models.CharField(max_length=100, unique=True, null=True,
                                   blank=True, verbose_name="Vendor Name")

    def __str__(self):
        return str(self.vendor_name)
