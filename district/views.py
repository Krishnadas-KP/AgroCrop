from django.shortcuts import render ,redirect
from django.http import HttpResponse
# Create your views here.



def districtwelcomepage(request) :

    if request.user.is_authenticated and (request.session['username']).startswith('D') :

        return render(request , 'district/welcome.html' , {'dname' : request.session['username'] })
        
    else :
    
        return redirect('/login')



