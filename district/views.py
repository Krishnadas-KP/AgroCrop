from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.db.models import Sum
import simplejson as json
import requests


from home.models import FarmerDetails , Local , Price , District , BuyerTransaction , FarmerTransaction ,Stock , Routes
def districtwelcomepage(request) :

    if request.user.is_authenticated and (request.session['username']).startswith('D') :
        
        district = District.objects.get(D_id = request.session['username'])
        return render(request , 'district/welcome.html' , {'dname' : district.D_Name  })
        
    else :
    
        return redirect('/login')




        
def transport(request):

    if request.user.is_authenticated :
    
        if request.method == "POST":
        
            TransportItem = request.POST.get('item')
            Source = request.POST.get('source')
            LCTotalQty = request.POST.get('quantity')
            
            #localCentersDest = Stock.objects.filter(Item_id__Item_Name = TransportItem , Quantity__lt = 10.0).order_by('Quantity')
            #print localCentersDest
            localCentersDest = Stock.objects.none()
            
            localCenters = Stock.objects.filter(L_id__D_id = request.session['username'],Item_id__Item_Name = TransportItem , Quantity__lt = 10.0).order_by('Quantity')
            
            for localCenter in localCenters :
            
                source = str(Source)
                dest = str(localCenter.L_id)
                url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins='+source+'&destinations='+dest+'&key=AIzaSyD-itnbYYRdntj6xMcEEB5TqU5kvyCntBw'
                r = requests.get(url)
                response = r.json()
                
                Strresult= json.dumps(response)
                result = json.loads(Strresult)
                
                distance = result['rows'][0]['elements'][0]['distance']['value']
                
                if float(distance) < 50000.0 :
                
                    x = localCenters.filter(L_id = localCenter.L_id)
                    localCentersDest = localCentersDest|x
            
            return render(request , 'state/transdest.html' ,{'localCenters' : localCentersDest , 'remain' : LCTotalQty , 'source' : Source , 'item' : TransportItem})
            
        localCentersSrc = Stock.objects.filter(L_id__D_id = request.session['username'] , Quantity__gt = 10.0 , WaitForAllocation = 0).order_by('-Quantity')
    
        return render(request , 'state/transport.html' , {'localCenters' : localCentersSrc} )
        
        
def StockAllocate(request) :

    if request.method == "POST" :
        source = request.POST.get('source')
        destn = request.POST.getlist('dest')
        item = request.POST.get('item')
        qty = request.POST.getlist('allocatedAmt')
        count = len(destn)
        i = 0
        L = Local.objects.get(L_Name = source)
        while(count > 0 ) :
            
            
            if float(qty[i]) <> 0.0 :   # To avoid allocaing 0 Kg in the Routes table

                
                D = Local.objects.get(L_Name = destn[i])
                
                
                RouteInstance = Routes.objects.create(src = L , dest = D , Item_Name = item , Quantity = float(qty[i]))
                RouteInstance.save()
                
            i = i + 1
            count = count - 1
            
        SourceToBlock = Stock.objects.get(L_id = L , Item_id__Item_Name = item )
        SourceToBlock.WaitForAllocation = 1
        SourceToBlock.save()
        
    return redirect('/district')
    
    
    
def payment(request):
    if request.user.is_authenticated:
    
        if request.method == "POST":
        
            Aadhaar =  request.POST.get('aadhaar')
            
            SelectedFarmer = FarmerDetails.objects.filter(Aadhaar = Aadhaar)
            Transactions = FarmerTransaction.objects.filter(Aadhaar = Aadhaar , L_id__D_id = request.session['username'])
            total = Transactions.aggregate(Sum('Amount'))
            
            return render(request , 'district/farmerAmount.html' , {'farmer' : SelectedFarmer[0] , 'Transactions' : Transactions , 'total' : total})
    
        
        farmers = FarmerTransaction.objects.filter(L_id__D_id = request.session['username']).order_by().values('Aadhaar').distinct()
        
        
        
            
        return render(request , 'district/payments.html' , {'farmers' : farmers})