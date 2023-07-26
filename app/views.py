from django.shortcuts import render
from app.froms import *
from app.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')


def registration(request):
    UFO = User_Form(label_suffix="")
    PFO = Profile_Form(label_suffix="")
    d = {'usfo':UFO,'pfo':PFO}

    if request.method=='POST' and request.FILES:
        usdf = User_Form(request.POST)
        pfd = Profile_Form(request.POST,request.FILES)

        if usdf.is_valid() and pfd.is_valid():
            NSUFO=usdf.save(commit=False)
            submittedPW = usdf.cleaned_data['password']
            NSUFO.set_password(submittedPW)
            NSUFO.save()

            NSPO = pfd.save(commit=False)
            NSPO.username=NSUFO
            NSPO.save()
            return HttpResponse('Sign Up Successful')
        else:
              return HttpResponse('Invalid Data')
    
    return render(request,'registration.html',d)


def user_login(request):
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        
        #authneication
        AUO = authenticate(username=un, password=pw)
        if AUO:
            
            #activate user checking and login request
            if AUO.is_active:
                login(request,AUO)
                request.session['username']=un
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Not a Active User")
        else:
            return HttpResponse('Invalid Details')
                
    return render(request, 'btnlogin.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required 
def display_details(request):
    username = request.session.get('username')
    UO = User.objects.get(username = username)
    PO = Profile.objects.get(username=UO)
    d = {'PO':PO,'UO':UO}
    return render(request,'display_details.html',d)