from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.http import Http404


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', locals())


@login_required(login_url='/accounts/login')
def home(request):
    current_user = request.user
    all_areas = Area.objects.all()

    return render(request, 'index.html', locals())


@login_required(login_url='/accounts/login')
def add_biz(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.uploaded_by = current_user
            image.save()
            return redirect('home')
    else:
        form = BusinessForm()
    return render(request, 'add-business.html', {'form': form})


@login_required(login_url='/accounts/login')
def area(request, area_id):
    businesses = Business.objects.all()
    try:
        area = Area.objects.get(id=area_id)
        result = Business.objects.filter(id=area_id)
        notices = Notification.objects.filter(id=area_id)
    except Area.DoesNotExist:
        raise Http404()
    return render(request, "neighborhood.html", locals())


@login_required(login_url='/accounts/login')
def edit_prof(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            lol = form.save(commit=False)
            lol.uploaded_by = current_user
            lol.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'profile_edit.html', {'profileform': form})


@login_required(login_url='/accounts/login')
def search_business(request):
    all_business = Business.objects.all()
    parameter = request.GET.get("business")
    result = Business.objects.filter(business_name__icontains=parameter)
    return render(request, 'search-businesses.html', locals())


@login_required(login_url='/accounts/login')
def logout_view(request):
    logout(request)



