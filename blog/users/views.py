from django.shortcuts import render, redirect
from  django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,userupdateform,profileupdateform
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'account created for {username} you can login now !')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form})

def login(request):
    if request.method=='POST':
        username = form.cleaned_data.get(username)
        password =form.cleaned_data.get(password)
        user = authenticate (request, username=username , password=password)
    if user is not None:
        login(request,user)
        return redirect('home')

@login_required
def profile(request):
    if request.method  =='POST':
        u_form =userupdateform(request.POST,request.FILES,instance=request.user)
        p_form =profileupdateform(instance=request.user.profile)
        if u_form.is_valid() and p_form.isvalid():
            u_form.save()
            p_form.save()
            messages.success(request,f'your account updated')
            return redirect ('profile')

    else:
        u_form =userupdateform(instance=request.user)
        p_form =profileupdateform(instance=request.user.profile)
    context ={'u_form' :u_form ,'p_form':p_form}
    return render(request,'users/profile.html', context)
