from django.shortcuts import render ,redirect
from django.http import HttpResponse

from forms import LocalAddForm
from home.models import FarmerDetails , Local , Price , District , BuyerTransaction , FarmerTransaction ,Stock , Routes
from django.contrib.auth.models import User

import json as simplejson , urllib


def statewelcomepage(request) :

    if request.user.is_authenticated and request.session['username'].startswith('a'):

        return render(request , 'state/homepage.html' , {} )
        
    else :
        
        return redirect('/login')


def setRates(request) :

    if request.user.is_authenticated and request.session['username'].startswith('a'):


        if request.method == "POST" :

            
            selectedItem = request.POST['search_text']

            itemDetails = Price.objects.filter(Item_Name = selectedItem)

          
            return render(request , 'state/rateSetForm.html', { 'itemDetails' : itemDetails , 'item' : itemDetails[0] } )

        items = Price.objects.order_by().values('Item_Name').distinct()
        return render(request , 'state/stateRateSet.html' , {'items' : items} )






def RateUpdater(request) :

    if request.method == "POST" :

        districtslist = District.objects.all()

        itemname = request.POST['item']
        

        for district in districtslist :

            val = request.POST.getlist(district.D_Name)
            
            item = Price.objects.get(Item_Name = itemname , D_id = district.D_id )
            item.Sell_Price = val[0]
            item.Buy_Price = val[1]
            item.save()
        
        return redirect('/state/rates')



def Confirmation(request) :
    

    verifiedUsers = FarmerDetails.objects.filter(VerifiedStatus = 1 , ConfirmedStatus = 0)

    if request.method == "POST" :
        
            person = request.POST.get('user')
            
            x = person.split(',')
            Aadhaar = x[0]
            item = x[1]
            local = x[2]

            
            
            localcenter = Local.objects.get(L_Name = local)
           
            
            items = Price.objects.get(D_id = localcenter.D_id , Item_Name = item)

        
            
            usersf = FarmerDetails.objects.get(Aadhaar = Aadhaar , L_id = localcenter , Item_id = items)
            
           
            usersf.ConfirmedStatus = 1
            usersf.save()
            

            return redirect('/state/confirm')




    return render(request , 'state/confirm.html' , {'users' : verifiedUsers } )





def transport(request):

    if request.user.is_authenticated :
    
        if request.method == "POST":
        
            TransportItem = request.POST.get('item')
            Source = request.POST.get('source')
            LCTotalQty = request.POST.get('quantity')
            
            
            localCentersDest = Stock.objects.none()
            
            localCenters = Stock.objects.filter(Item_id__Item_Name = TransportItem , Quantity__lt = 10.0).order_by('Quantity')
            
            for localCenter in localCenters :
            
                source = str(Source)
                dest = str(localCenter.L_id)
                
                url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins='+source+'&destinations='+dest+'&key=AIzaSyD-itnbYYRdntj6xMcEEB5TqU5kvyCntBw'
                
                result= simplejson.load(urllib.urlopen(url))
                distance = result['rows'][0]['elements'][0]['distance']['value']
            
                if float(distance) < 50000.0 :
                
                    x = localCenters.filter(L_id = localCenter.L_id)
                    localCentersDest = localCentersDest|x
            
            return render(request , 'state/transdest.html' ,{'localCenters' : localCentersDest , 'remain' : LCTotalQty , 'source' : Source , 'item' : TransportItem})
            
        localCentersSrc = Stock.objects.filter(Quantity__gt = 10.0).order_by('-Quantity')
    
        return render(request , 'state/transport.html' , {'localCenters' : localCentersSrc} )



def StockAllocate(request) :

    if request.method == "POST" :
    
        source = request.POST.get('source')
        destn = request.POST.getlist('dest')
        item = request.POST.get('item')
        qty = request.POST.getlist('allocatedAmt')
        count = len(destn)
        i = 0
        while(count > 0 ) :
            
            
            if int(qty[i]) <> 0 :   # To avoid allocaing 0 Kg in the Routes table
               
                L = Local.objects.get(L_Name = source)
                D = Local.objects.get(L_Name = destn[i])
                
                
                RouteInstance = Routes.objects.create(src = L , dest = D , Item_Name = item , Quantity = qty[i])
                RouteInstance.save()
                
            i = i + 1
            count = count - 1
            
        
    return redirect('/state')

        

def deleteUser(request):

    if request.method == "POST" :
        id = request.POST.get('id')
        instance = FarmerDetails.objects.get(id = id)
        instance.delete()
        
    return redirect('/state/confirm')   
    



def addLocal(request):
    if request.user.is_authenticated and request.session['username'].startswith('a'):
        
        form = LocalAddForm(request.POST or None)
        if form.is_valid():
            LocCenName = request.POST.get('LName')
          
            DistrictID = request.POST.get('District')
            
            pwd = request.POST.get('password')
            
            DistInst = District.objects.get(D_id = DistrictID)
            LastLocal = Local.objects.last()
            LastId =  int((LastLocal.L_id).split('L')[1])
            LastId = LastId + 1
            x =  "%04d" % (LastId)
            NewID = 'L' + str(x)
            NewLocalCenter = Local.objects.create(L_id = NewID , L_Name = LocCenName , D_id = DistInst)
            NewLocalCenter.save()
            
            user = User.objects.create_user(username=NewID, password=pwd)
            user.save()
            
            
            Items = Price.objects.filter(D_id = DistInst)
            
            
            
            for item in Items :
            
                InitStock = Stock.objects.create(L_id = NewLocalCenter , Item_id = item , Quantity = 0.0)
                InitStock.save()
                
            
            return redirect('/state')
            
        return render(request , 'state/addlocal.html' , {'form' : form})


def addItem(request):

    if request.user.is_authenticated and request.session['username'].startswith('a'):
    
        
        DistList = District.objects.all()
        if request.method == "POST" :
        
            itemName = request.POST.get('IName')
            LastItem = Price.objects.last()
            LastId =  int((LastItem.Item_id).split('I')[1])
            LastId = LastId + 1
            x =  "%04d" % (LastId)
            NewID = 'I' + str(x)
            
            
            for district in DistList:
                
                prices = request.POST.getlist(district.D_id)
                NewItem = Price.objects.create(Item_id = NewID , Item_Name = itemName , D_id = district , Buy_Price = prices[0] , Sell_Price = prices[1])
                NewItem.save()
                
                LocalCenters = Local.objects.filter(D_id = district)
                for LocalCenter in LocalCenters :
                    newItemLocalStock = Stock.objects.create(L_id = LocalCenter , Item_id = NewItem , Quantity = 0.0)
                    newItemLocalStock.save()
                    
                    
            return redirect('/state')
        return render(request , 'state/additem.html' , {'Districts' : DistList})


