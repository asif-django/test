from django.db import models

# Create your models here.


GRN_TYPES = (('A', 'A'), ('B', 'B'), ('C', 'C'))

STORES = (('Ramnagar', 'Ramnagar'), ('B', 'ABCD'), ('C', 'XYZ'))

PYMENT_TYPE = (('Cash','Cash'),('Card', 'Card'),('UPI', 'UPI'), ('Others', 'Others'))


class Goods(models.Model):
    grn_type = models.CharField(max_length=50, null=True, blank=True, choices=GRN_TYPES, verbose_name="GRN_Type" )
    received_store = models.CharField(max_length=50, null=True, blank=True, choices=STORES, verbose_name="Received Store")
    vendor_supplier = models.CharField(max_length=50, null=True, blank=True, verbose_name="Vendor/Supplier")
    invoice_no = models.CharField(max_length=100, null=True, blank=True, verbose_name="D/C or Invoice No")
    received_date = models.DateField(null=True, blank=True, verbose_name="Received Date")
    received_by = models.CharField(max_length=50, blank=True, null=True, verbose_name="Received By")
    invoice_date = models.DateField(null=True, blank=True, verbose_name="Invoice Date")
    invoice_amount = models.FloatField(null=True, blank=True, verbose_name="Invoice Amount")
    gst_amount = models.FloatField(null=True, blank=True, verbose_name="GST Amount")
    remarks = models.CharField(max_length=150, null=True, blank=True, verbose_name="Remarks")
    net_amount = models.FloatField(null=True, blank=True, verbose_name="Net_Amount")
    round_off = models.IntegerField(null=True, blank=True, verbose_name="Round Off")

    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Goods"
        verbose_name = "Goods"
    
    def __str__(self):
        return str(self.vendor_supplier)


class Medicine(models.Model):
    vendor_supplier = models.ForeignKey(Goods, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Item Name")
    quantity = models.IntegerField(null=True, blank=True, verbose_name="Quantity")
    free_quantity = models.IntegerField(null=True, blank=True, verbose_name="Free Quantity")
    batch_id = models.CharField(max_length=50, null=True, blank=True, verbose_name="Batch ID")
    expiry_date = models.DateField(null=True, blank=True, verbose_name="Expiry Date")
    sale_price = models.FloatField(null=True, blank=True, verbose_name="Sale Price")
    cost_price = models.FloatField(null=True, blank=True, verbose_name="Cost Price")
    gst = models.FloatField(null=True, blank=True, verbose_name="GST(%)")
    sub_total = models.FloatField(null=True, blank=True, verbose_name="Sub Total")

    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Medicines"
        verbose_name = "Medicine"
    
    def __str__(self):
        return str(self.vendor_supplier)


class Sale(models.Model):
    store = models.CharField(max_length=50, null=True, blank=True, choices=STORES, verbose_name="Store")
    bill_no = models.CharField(max_length=50, null=True, blank=True, verbose_name="Bill_No")
    patient = models.CharField(max_length=50, null=True, blank=True, verbose_name="Patien Name")
    phone = models.CharField(max_length=50, null=True, blank=True, verbose_name="Mobile Number")
    referred_by = models.CharField(max_length=50, null=True, blank=True, verbose_name="Referred By")
    payment_type = models.CharField(max_length=50, null=True, blank=True, choices=PYMENT_TYPE, verbose_name="Payment Type")
    total_vat = models.FloatField(null=True, blank=True, verbose_name="GST Amount")
    net_amount = models.FloatField(null=True, blank=True, verbose_name="Net_Amount")
    total_amount = models.FloatField(null=True, blank=True, verbose_name="Total_Amountt")
    
    

    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Sales"
        verbose_name = "Sale"
    
    def __str__(self):
        return self.patient
    


class Sale_Items(models.Model):
    patiant_name = models.ForeignKey(Sale,  on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Item Name")
    quantity = models.IntegerField(null=True, blank=True, verbose_name="Quantity")    
    batch_id = models.CharField(max_length=50, null=True, blank=True, verbose_name="Batch ID")
    unit_price = models.FloatField(null=True, blank=True, verbose_name="Unit Price")
    discount = models.FloatField(null=True, blank=True, verbose_name="Discount")
    gst = models.FloatField(null=True, blank=True, verbose_name="GST(%)")
    sub_total = models.FloatField(null=True, blank=True, verbose_name="Sub Total")

    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Sale_Items"
        verbose_name = "Sale_Item"
    
    def __str__(self):
        return self.item_name