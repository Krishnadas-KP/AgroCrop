from django.shortcuts import render ,redirect
from django.http import HttpResponse
# Create your views here.
import json as simplejson , urllib

from home.models import FarmerDetails , Local , Price , District , BuyerTransaction , FarmerTransaction ,Stock , Routes
def districtwelcomepage(request) :

    if request.user.is_authenticated and (request.session['username']).startswith('D') :

        return render(request , 'district/welcome.html' , {'dname' : request.session['username'] })
        
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
                result= simplejson.load(urllib.urlopen(url))
                distance = result['rows'][0]['elements'][0]['distance']['value']
                
                if float(distance) < 50000.0 :
                
                    x = localCenters.filter(L_id = localCenter.L_id)
                    localCentersDest = localCentersDest|x
            
            return render(request , 'state/transdest.html' ,{'localCenters' : localCentersDest , 'remain' : LCTotalQty , 'source' : Source , 'item' : TransportItem})
            
        localCentersSrc = Stock.objects.filter(L_id__D_id = request.session['username'] , Quantity__gt = 10.0).order_by('-Quantity')
    
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
            
        
    return redirect('/district')