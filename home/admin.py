from django.contrib import admin
from .models import District,Local,Price,FarmerDetails,FarmerTransaction , BuyerTransaction , Stock , Routes



class DistrictAdmin(admin.ModelAdmin) :
    list_display = ['D_id', 'D_Name' ,'C_Date']


admin.site.register(District , DistrictAdmin)


class LocalAdmin(admin.ModelAdmin) :
    list_display = ['L_id', 'L_Name' ,'D_id','C_Date']


admin.site.register(Local , LocalAdmin)

class PriceAdmin(admin.ModelAdmin) :
    list_display = ['Item_id','Item_Name','D_id','Buy_Price','Sell_Price']

admin.site.register(Price,PriceAdmin)

class FarmerDetailsAdmin(admin.ModelAdmin) :
    list_display = ['id','Aadhaar','F_Name','F_Addr','L_id','Item_id', 'Bank' ,'IFSC' , 'AC_NO' , 'Apply_Date' , 'VerifiedStatus' ,  'ConfirmedStatus']

admin.site.register(FarmerDetails,FarmerDetailsAdmin)


class FarmerTransactionAdmin(admin.ModelAdmin) :

    list_display = ['id' , 'Aadhaar' ,'L_id' ,'Item_id' , 'Quantity' , 'Rate' , 'Amount' , 'Transaction_Date']

admin.site.register(FarmerTransaction , FarmerTransactionAdmin)


class BuyerTransactionAdmin(admin.ModelAdmin) :
    list_display = ['L_id' , 'Item_id', 'Quantity' ,'Rate' , 'Amount','Transaction_Date']


admin.site.register(BuyerTransaction , BuyerTransactionAdmin)


class StockAdmin(admin.ModelAdmin) :
    list_display = ['L_id', 'Item_id' ,'Quantity']


admin.site.register(Stock , StockAdmin)



class RoutesAdmin(admin.ModelAdmin) :
    list_display = ['src', 'dest' ,'Item_id' ,'Quantity' ,'Transaction_Date' ]


admin.site.register(Routes , RoutesAdmin)
