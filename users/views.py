from django.shortcuts import render,redirect
from .forms import RegisterForm,Updateform,Profileform
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            messages.success(request,f'your account has been created {username}')
            return redirect("login")
    else:
        form=RegisterForm()
    return render(request,"users/register.html",{"form":form})
@login_required
def profile(request):
    if request.method=="POST":
        u_form=Updateform(request.POST,instance=request.user)
        p_form=Profileform(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,"your profile has been updated")
            return redirect("profile")
    else:
        u_form=Updateform()
        p_form=Profileform()


    context={
        'u':u_form,
        'p':p_form
    }
    return render(request,"users/profile.html",context)
def manual_logout(request):
    logout(request)  
    messages.success(request, "You have been logged out successfully!")
    return redirect('home')  