from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import CreateView
from .models import User1
from .forms import PatientSignUpForm, DoctorSignUpForm, StaffSignUpForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

class patient_register(CreateView):
    model = User1
    form_class = PatientSignUpForm
    template_name= 'patient_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/home')

class doctor_register(CreateView):
    model = User1  
    form_class = DoctorSignUpForm
    template_name= 'doctor_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/home')


class staff_register(CreateView):
    model = User1  
    form_class = StaffSignUpForm
    template_name= 'staff_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/home')

def login_user(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/accounts/home')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, 'login.html',context={'form':AuthenticationForm()})

def logout_user(request):
    logout(request)
    return redirect('/accounts/home')


# Create your views here.
