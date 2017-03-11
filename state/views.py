from django.shortcuts import render ,redirect
from django.http import HttpResponse

from home.models import FarmerDetails , Local , Price , District , BuyerTransaction , FarmerTransaction ,Stock


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




















