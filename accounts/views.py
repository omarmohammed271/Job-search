from django.shortcuts import redirect, render
from django.urls import reverse
from .form import SignForm,USerForm,ProfileForm
from django.contrib.auth import authenticate,login
from .models import Profile

# Create your views here.
def signup(request):

    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = SignForm()

    return render(request,'registration/signup.html',{'form':form})

def profile(request):
    pro = Profile.objects.get(user = request.user)

    return render(request,'acc/profile.html',{'p':pro})

def profile_edit(request):
    profile = Profile.objects.get(user = request.user)

    if request.method == 'POST':
        u = USerForm(request.POST,request.FILES,instance=request.user)
        p = ProfileForm(request.POST,request.FILES,instance=profile)
        if u.is_valid() and p.is_valid():
            u.save()
            myprofile = p.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else:
        u = USerForm(instance=request.user)
        p = ProfileForm(instance=profile)

    

    return render(request,'acc/profile_edit.html',{'u':u , 'p':p})

def base(request):
    base = Profile.objects.get(user = request.user)

    
    return render(request,'base.html',{'base':base})
