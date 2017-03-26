from __future__ import unicode_literals

from django.db import models

# Create your models here.



class District(models.Model):
    D_id = models.CharField(max_length = 10, primary_key = True)
    D_Name = models.CharField(max_length = 20)
    C_Date = models.DateTimeField(auto_now = False , auto_now_add = True)


    def __unicode__ (self):
        return self.D_Name

    def __str__ (self):
        return self.D_Name


class Local(models.Model):
    L_id = models.CharField(max_length = 10, primary_key = True)
    L_Name = models.CharField(max_length = 20)
    D_id = models.ForeignKey(District, on_delete=models.CASCADE)
    C_Date = models.DateTimeField(auto_now = False , auto_now_add = True)


    def __unicode__ (self):
        return self.L_Name

    def __str__ (self):
        return self.L_Name


class Price(models.Model):

    Item_id = models.CharField(max_length=10)
    Item_Name = models.CharField(max_length = 50)
    D_id = models.ForeignKey(District, on_delete=models.CASCADE)
    Buy_Price = models.IntegerField()
    Sell_Price = models.IntegerField()

    def __unicode__ (self):
        return self.Item_Name

    def __str__ (self):
        return self.Item_Name


class FarmerDetails(models.Model) :

    Aadhaar = models.CharField(max_length = 12)
    F_Name = models.CharField(max_length = 50)
    AadhaarPic = models.FileField()
    doc = models.FileField()
    F_Addr = models.TextField(max_length = 150)
    F_Ph_NO = models.CharField(max_length = 15)
    L_id = models.ForeignKey(Local, on_delete=models.CASCADE)
    Item_id = models.ForeignKey(Price, on_delete=models.CASCADE)
    AC_NO = models.CharField(max_length = 16)
    Bank = models.CharField(max_length = 15)
    IFSC = models.CharField(max_length = 11)
    Apply_Date = models.DateTimeField(auto_now = False , auto_now_add = True)
    VerifiedStatus = models.CharField(max_length=1 , default="0") #1 for Yes 0 for No
    ConfirmedStatus = models.CharField(max_length=1 , default="0") #1 for Yes 0 for No

    

    def __unicode__ (self):
        return self.Aadhaar

    def __str__ (self):
        return self.Aadhaar


class FarmerTransaction(models.Model) :

    

    L_id = models.ForeignKey(Local, on_delete=models.CASCADE)
    Aadhaar = models.CharField(max_length = 12)
    Item_id = models.ForeignKey(Price, on_delete=models.CASCADE)
    Quantity = models.FloatField()
    Rate = models.FloatField()
    Amount = models.FloatField()
    Transaction_Date = models.DateTimeField(auto_now = False , auto_now_add = True)

    def __unicode__ (self):
        return self.Aadhaar

    def __str__ (self):
        return self.Aadhaar
        
class BuyerTransaction(models.Model) :

    L_id = models.ForeignKey(Local, on_delete=models.CASCADE)
    Item_id = models.ForeignKey(Price, on_delete=models.CASCADE)
    Quantity = models.FloatField()
    Rate = models.FloatField()
    Amount = models.FloatField()
    Transaction_Date = models.DateTimeField(auto_now = False , auto_now_add = True)

    def __unicode__ (self):
        return '%s' % (self.L_id)

    def __str__ (self):
        return '%s' % (self.L_id)


    
        
        
class Stock(models.Model) :

    L_id = models.ForeignKey(Local, on_delete=models.CASCADE)
    Item_id = models.ForeignKey(Price, on_delete=models.CASCADE)
    Quantity = models.FloatField()
    
    
    def __unicode__ (self):
        return '%s' % (self.L_id)

    def __str__ (self):
        return '%s' % (self.L_id)
        
class Routes(models.Model) :

    src = models.ForeignKey(Local, related_name='source', on_delete=models.CASCADE)
    dest = models.ForeignKey(Local,related_name='destination', on_delete=models.CASCADE)
    Item_id = models.ForeignKey(Price, on_delete=models.CASCADE)
    Quantity = models.FloatField()
    Transaction_Date = models.DateTimeField(auto_now = False , auto_now_add = True)
    
    def __unicode__ (self):
        return '%s' % (self.src)

    def __str__ (self):
        return '%s' % (self.src)


