
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import FormView,CreateView,ListView,TemplateView,View
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .models import Room
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
import datetime
from manager.urls import*



# class CustomLoginView(LoginView):
#     template_name = 'lg.html'  


class HomeView(FormView):
    template_name="home.html"
    form_class=LoginForm
    def post(self,request,*args,**kwargs):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            us=form_data.cleaned_data.get("username")   
            pswd=form_data.cleaned_data.get("password")   
            user=authenticate(request,username=us,password=pswd)
            if user.is_superuser:
                login(request,user)
                messages.success(request,'login successfully')
                return redirect('Mhome')
            elif user:
                login(request,user)
                messages.success(request,'login successfully')
                return redirect('ghm')
            else:
                messages.error(request,"login failed")
                return redirect('hm')
        return render(request,"home.html",{"form":form_data})



class Userregview(CreateView):
    template_name='register.html'
    form_class=RegForm
    model=User
    success_url=reverse_lazy('home')


    def form_valid(self, form):
        messages.success(self.request,"Registration successfull")
        return super().form_valid(form)


class Ghome(TemplateView):
    template_name = "guesthome.html"



