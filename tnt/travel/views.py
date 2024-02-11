from django.shortcuts import render, redirect
from django.http import HttpResponse
from travel.models import user
from travel.forms import UserForm

# Create your views here.
def test(request):
    return HttpResponse("Hello !")
    
def loginf(request):
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		check_user = user.objects.filter(email = email)
		valid_user = (len(list(check_user)) == 1)
		if (valid_user):
			current_user = email
			username = check_user.first().username
			request.session['current_user'] = current_user
			request.session['username'] = username
			return render(request, 'login.html', {'msg': 'Login successful'})
		else:
			return render(request, 'login.html', {'msg': 'Failed. Please try again'})
	else:
		return render(request, 'login.html')
        
def welcome(request):
    return render(request,'welcome.html')
    
def domestic(request):
    return render(request,'domestic.html')
    
def international(request):
    return render(request,'international.html')
    
def kerala(request):
    return render(request,'Kerala.html')
    
def Rajasthan(request):
    return render(request,'Rajasthan.html')
    
def Kashmir(request):
    return render(request,'Kashmir.html')
    
def Dubai(request):
    return render(request,'Dubai.html')
    
def Singapore(request):
    return render(request,'Singapore.html')
    
def Europe(request):
    return render(request,'Europe.html')
    
def gallery(request):
    return render(request,'gallery.html')
    
def about(request):
    return render(request,'about.html')
    
def signup(request):
    return render(request,'signup.html')
    
def sign(request):
    if request.method=="POST":
        f=UserForm(request.POST)
        if f.is_valid():
            try:
                f.save()
                return redirect('../travel/login/')
            except:
                pass 
        else:
            f=UserForm()
    return render(request,'signup.html')
    
def show(request):
    s=user.objects.all()
    return render(request,'show.html', {'b':s})
    
def edit(request,id):
    z=user.objects.get(id=id)
    return render(request,'edit.html', {'b':z})
    
def edcode(request,id):
    h=user.objects.get(id=id)
    form=UserForm(request.POST, instance=h)
    if form.is_valid():
        form.save()
        return redirect("../show")
    return render(request,'edit.html', {'b':h})
    
def login(request):
    return render(request,'login.html')
    
def buynow(request):
    return render(request,'buynow.html')
    
    
def log(request):
    if request.method=='POST':
            email=request.POST['email']
            username=request.POST['username']
            password=request.POST['password']
            try:
                h=user.objects.get(email=email)
                c=user.objects.get(password=password)
                k=user.objects.get(username=username)
                if h and c and k is not None:
                    return render(request,'welcome.html',{'z':h})
                else:
                    return render(request,'login.html')
            except:
                return render(request,'login.html')
    
    
