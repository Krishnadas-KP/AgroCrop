from django.shortcuts import render ,redirect
from django.http import HttpResponse

from home.models import FarmerDetails , Local , Price , District , BuyerTransaction , FarmerTransaction ,Stock , Routes


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


        return render(request , 'state/stateRateSet.html' , {} )






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
            
            localCentersDest = Stock.objects.filter(Item_id__Item_Name = TransportItem , Quantity__lt = 10.0).order_by('Quantity')
            
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
            
            print qty[i]
            if qty[i] <> 0 :
                #RouteInstance = Routes(src__L_Name = source , dest__L_Name = destn[i] , Item_id__Item_Name = item , Quantity = qty[i])
                
                
                L = Local.objects.get(L_Name = source)
                D = Local.objects.get(L_Name = destn[i])
                #I = Price.objects.filter(Item_Name = item).distinct()
                
                RouteInstance = Routes.objects.create(src = L , dest = D , Item_Name = item , Quantity = qty[i])
                RouteInstance.save()
                
                i = i + 1
                count = count - 1
           
        
    return redirect('/state')

        








