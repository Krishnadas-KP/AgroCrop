from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


from home.models import FarmerDetails , Local , Price , District , BuyerTransaction , FarmerTransaction ,Stock,Routes






def localwelcomepage(request):

    if request.user.is_authenticated:
        name = request.session['username']
        
        lname  = Local.objects.get(L_id = name)

        count = Routes.objects.filter(src = name).count()

        return render(request, 'local/welcome.html', {'name' : name , 'lname':lname.L_Name , 'count' : count })
    return redirect('/login')
    
    
    
    
    
    

def verification(request) :
    if request.user.is_authenticated:
    
        name = Local.objects.get(L_id = request.session['username'] )
        
        if request.method == "POST" :
        
            
            person = request.POST.get('user')
            
            x = person.split(',')
            item = x[1]

            
            
            items = Price.objects.get(D_id = name.D_id , Item_Name = item)

        
            
            
            
            usersf = FarmerDetails.objects.get(Aadhaar = x[0] , L_id = request.session['username'] , Item_id = items)
            
           
            usersf.VerifiedStatus = 1
            usersf.save()
            

            return redirect('/local')
    
            

    
        
        users = FarmerDetails.objects.filter(L_id = request.session['username'] , VerifiedStatus = 0).order_by('Apply_Date')
        
        
        return render(request, 'local/verify.html' ,{'users' : users , 'name':name})
    
    return redirect('/login')
    

    
def search_users_verify(request) :
    
    if request.method == "POST" :
        search_text = request.POST['search_text']
    else :
        search_text = ''
        
    users = FarmerDetails.objects.filter(Aadhaar__contains = search_text , VerifiedStatus = 0 , L_id = request.session['username'])
    return render(request , 'local/search_users_list.html' , {'users' : users })
    


    
def buyvegetables(request) :

    if request.user.is_authenticated:
    
        name = Local.objects.get(L_id = request.session['username'] )
        
        if request.method == "POST" :
        
            Aadhaar = request.POST['search_data']
            
           
            user = FarmerDetails.objects.filter(Aadhaar = Aadhaar ,L_id = request.session['username'], ConfirmedStatus = 1)
            
            if not user :
                return HttpResponse("No Users Found :(")

            items = Price.objects.none() #Create an empty queryset

            for x in user :
                
                item = Price.objects.filter(Item_Name = x.Item_id , D_id = name.D_id)

                items = items|item #Append Queryset item to items
                
            

            return render(request, 'local/farmerItemList.html' , { 'Aadhaar' : Aadhaar , 'items' : items})
            
            

            return redirect('/local')
    
            

    
        
        
        
        
        return render(request, 'local/buy.html' ,{'name':name})
    
    return redirect('/login')

def pollingData(request) :

    

    LocalCenter = request.session['username']

    count = Routes.objects.filter(src = LocalCenter).count()
    
    return HttpResponse(count)

    
    
    

def CollectFarmerItems(request) :

    localcenter = Local.objects.get(L_id = request.session['username'])
    Item = Price.objects.filter(D_id = localcenter.D_id)

    if request.method == "POST" :

        
            items = request.POST.getlist('item')
            rates = request.POST.getlist('rate')
            qtty = request.POST.getlist('qty')
            amnt = request.POST.getlist('amt')
            userAadhaar = request.POST.get('user')
            
            
            i = 0
            count = len(amnt)
            
            while i<count :
            
                itm = Price.objects.get(Item_id = items[i].split(',')[0] , D_id = localcenter.D_id)
                
                instance = FarmerTransaction.objects.create(L_id = localcenter , Aadhaar = userAadhaar , Item_id = itm , Quantity = qtty[i] , Rate = rates[i] , Amount = amnt[i])
                instance.save()
                
                stock = Stock.objects.get(L_id = localcenter , Item_id = itm)
                
                stock.Quantity = float(stock.Quantity) + float(qtty[i])
                stock.save()
                i = i+1
          
            return redirect('/local')   


    
    
    
    
    

def sellvegetables(request) :

    if request.user.is_authenticated:
    
        Dist = Local.objects.get(L_id = request.session['username'])
        Item = Price.objects.filter(D_id = Dist.D_id)
        
        if request.method == "POST" :
        
            items = request.POST.getlist('item')
            rates = request.POST.getlist('rate')
            qtty = request.POST.getlist('qty')
            amnt = request.POST.getlist('amt')
            i = 0
            count = len(amnt)
            
            while i<count :
            
                itm = Price.objects.get(Item_id = items[i].split(',')[0] , D_id = Dist.D_id)
                
                instance = BuyerTransaction.objects.create(L_id = Dist , Item_id = itm , Quantity = qtty[i] , Rate = rates[i] , Amount = amnt[i])
                instance.save()
                
                stock = Stock.objects.get(L_id = Dist , Item_id = itm)
                
                stock.Quantity = float(stock.Quantity) - float(qtty[i])
                stock.save()
                i = i+1
          
            return redirect('/local')
            
            
        
        return render(request, 'local/sell.html' , {'dis' : Dist.D_id , 'items' : Item})
    return redirect('/login')


def amtfinder(request):

    if request.method == "POST" :

     
    
        qty = request.POST['search_data']
        rate = request.POST['rate']
        
        if(qty == ''):
            qty = 0
            
        amount = float(qty)*float(rate)
        
        
        return HttpResponse(amount)
       
       
        
        
          
    
    
    
    
    


def checkrates(request) :

    if request.user.is_authenticated:
    
        local = Local.objects.get(L_id = request.session['username'])
        items = Price.objects.filter(D_id = local.D_id).distinct()
        
        
        return render(request, 'local/rates.html' , {'items' : items})
    return redirect('/login')


    
    
    
    
    
    
    
    

def transport(request) :

    if request.user.is_authenticated:
        return render(request, 'local/transport.html' , {})
    return redirect('/login')
