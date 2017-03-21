from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth import (
    authenticate ,
    login ,
    logout
)

from .forms import LoginForm , RegForm
from .models import Local , District , Price , FarmerDetails
def welcomepage(request) :

    # AGROCROP front page

    return render(request , 'home/index.html' , {})

#This is a test comment for github commit

def loginform(request) :

    form = LoginForm(request.POST or None)
    message = "LOGIN"
    form_class = "alert alert-success"
    if form.is_valid():

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")


        user = authenticate(username=username , password=password)

        if not user :
            message = "Username or Password Wrong"
            form_class = "alert alert-danger"
            return render(request , 'home/login.html' , {'form' : form , 'message' : message , 'class' : form_class})
        else :

            request.session['username'] = username
            login(request,user)
            
            if username.startswith('L') :
                return redirect('/local')
            elif username.startswith('D') :
                return redirect('/district')
            else :
                return redirect('/state')
         

    return render(request , 'home/login.html' , {'form' : form , 'message' : message, 'class' : form_class})




def registration(request) :
    
    form = RegForm(request.POST or None)
    
    queryset = Price.objects.all().values('Item_Name').distinct()
    districtset = District.objects.all().values('D_Name').distinct()
    if form.is_valid():
    
        Aadhaar = form.cleaned_data.get("Aadhaar")
        Address = form.cleaned_data.get("Address")
        name = form.cleaned_data.get("Name")
        mobNum = form.cleaned_data.get("mobNum")
        ACnum = form.cleaned_data.get("ACnum")
        Bank = form.cleaned_data.get("Bank")
        IFSC = form.cleaned_data.get("IFSC")
        documents = request.FILES.getlist("farmdoc")
        Aadhaarpic = request.FILES.get("aadhaarpic")
        
        
      
        districts = request.POST.getlist('district')   
        items = request.POST.getlist('item')
        nearestLocal = request.POST.getlist('local')
        i = 0
        count = int(request.POST.get('count'))
        
        while count > 0 :
            
            district = District.objects.get(D_Name = districts[i])
   
            Item = Price.objects.get(Item_Name = items[i] , D_id = district.D_id)
          
            Locals = Local.objects.get(L_Name = nearestLocal[i])

            farmer = FarmerDetails.objects.create(Aadhaar = Aadhaar , F_Name = name ,AadhaarPic = Aadhaarpic, doc = documents[i] ,F_Addr = Address , F_Ph_NO = mobNum ,L_id = Locals, Item_id = Item , Bank = Bank , AC_NO = ACnum , IFSC = IFSC , VerifiedStatus = 0 , ConfirmedStatus = 0)
            farmer.save()
            i = i+1
            count = count-1  
        
        
        return render(request , 'home/regConfirm.html' , {'name' : name})
        
        
    
 
    return render(request , 'home/register.html' , {'PForm' : form , 'queryset' : queryset , 'districtset' : districtset})
    
    
    
def reglogic(request) :

    if request.method == "POST" :
        search_text = request.POST['search_text']
        
        var = search_text
    else :
        search_text = ''
    dist = District.objects.get(D_Name = var)
    nearestLocal = Local.objects.filter(D_id = dist.D_id)
    
   
    
    return render(request , 'home/dynpop.html' , {'locals' : nearestLocal , 'var' : var})
    

def rates(request) :
    
    if request.method == "POST" :
        
        search_text = request.POST['search_data']
        
        items = Price.objects.filter(D_id = search_text).distinct()
        
        return render(request , 'home/ratetable.html' ,{'items' : items})
    
    districts = District.objects.all()
    return render(request , 'home/rates.html' , {'districts' : districts})


def logout_view(request):

    logout(request)
    return redirect('/')















