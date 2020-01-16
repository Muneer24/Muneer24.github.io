from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView
from django.views import generic
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from search_views.search import SearchListView
from .models import Product
from .forms import UserForm
from base.forms import UserForm
from rest_framework.decorators import api_view
from categories.models import Category

class Index(generic.ListView):
    template_name = "base/index.html"
    context_object_name = "product"

    def get_queryset(self):
        return Product.objects.all()


def detail(request,slug):
    products = ProductModel.objects.filter(active=True)
    categories = CategoryModel.objects.filer(active=True)
    if request.method =="POST":
        form =ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, "Review saved")
        else:
            messages.error(request, "invalid form")
    else:
        form =ReviewForm()

    context = {"product" : product, "products" : products,  "catergories" : categories, "title":cat.name + " - Categories", "form" : form}

    return render(request, "base/detail.html", context)

class Contact_Us(TemplateView):
    template_name = "base/contact-us.html"

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return redirect('base:index')

@login_required
def profile(request):
    return render(request, 'base/profile.html')
       
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = user_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'base/index.html',
                          {'user_form':user_form,
                           'registered':registered})
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('base:index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'base/index.html', {})

def get_category(request, slug):
    selected_category= get_object_or_404(Category, slug=slug)
    return render (request, 'base/shop.html',
        {'category':selected_category},
        {'business':Business.objects.all()})

