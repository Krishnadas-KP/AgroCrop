from django.shortcuts import render ,redirect
from django.http import HttpResponse

from home.models import Price , District


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
























