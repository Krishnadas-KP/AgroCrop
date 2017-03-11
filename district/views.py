from django.shortcuts import render ,redirect
from django.http import HttpResponse
# Create your views here.



def districtwelcomepage(request) :

    if request.user.is_authenticated and (request.session['username']).startswith('D') :

        return HttpResponse("<h1> District Welcome Page </h1>")
        
    else :
    
        return redirect('/login')