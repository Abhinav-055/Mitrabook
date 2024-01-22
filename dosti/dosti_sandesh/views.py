from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseNotFound
from .forms import NewuserForm
from .models import Newuser
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    return render(request,'dosti_sandesh/login.html')
def login_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
           user=Newuser.objects.get(username=username)
        except Newuser.DoesNotExist:
            return render(request,"dosti_sandesh/user_not_found.html")
        if user is not None:
            password1=user.password
            username=user.username
            context={}
            if password==password1:
                for field in user._meta.fields:
                   field_name = field.name
                   field_value = getattr(user, field_name)
                   context[field_name] = field_value
                return render(request,'dosti_sandesh/home.html',context)
            else:
                return HttpResponse('Incorrect password')
        else:
            return render(request,"dosti_sandesh/user_not_found.html")
def createuser(request):
    form = NewuserForm()
    if request.method == 'POST':
        form = NewuserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'dosti_sandesh/user_registration_done.html')
    context = {'form':form}
    return render(request,'dosti_sandesh/new_user_registration.html',context)
def search(request):
    context={}
    if request.method=='POST':
        username1=request.POST.get("q")
        current_user = request.POST.get("current_user")
        if username1==current_user:
            return HttpResponse("Cant search your own profile")
        try:
            userinfo=Newuser.objects.get(username=username1)
        except Newuser.DoesNotExist:
            return HttpResponse("User not found")
        for field in userinfo._meta.fields:
            field_name = field.name
            field_value = getattr(userinfo, field_name)
            context[field_name] = field_value
        return render(request,'dosti_sandesh/profile.html',context)
def chat(request):
    return render(request,'dosti_sandesh/chat.html')


        