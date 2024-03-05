from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django import forms

from world_of_speed.cars.models import Car
from world_of_speed.profiles.models import Profile
from world_of_speed.web.views import get_profile


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture']

        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']

        widgets = {
            'password': forms.PasswordInput(render_value=True)
        }


def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'form': form}

    return render(request, 'profiles/profile-create.html', context)


def profile_details(request):
    profile = get_profile()
    total_price = profile.car_set.aggregate(total_price=Sum('price'))['total_price']
    context = {
        'profile': profile,
        'total_price': total_price
    }
    return render(request, 'profiles/profile-details.html', context)


def profile_edit(request):
    profile = get_profile()
    form = ProfileEditForm(request.POST or None, instance=profile)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile-details')

    context = {'form': form, 'profile': profile}

    return render(request, 'profiles/profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()

    if request.method == 'POST':
        profile.delete()
        return redirect('index')
    context = {
        'profile': profile
    }
    return render(request, 'profiles/profile-delete.html', context)
