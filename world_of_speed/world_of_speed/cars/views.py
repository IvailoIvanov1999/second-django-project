from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, DeleteView, UpdateView

from world_of_speed.cars.models import Car
from world_of_speed.web.views import get_profile


class CarEditForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_type', 'car_model', 'year', 'image_url', 'price']

        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_type', 'car_model', 'year', 'image_url', 'price']

        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }


def create_car(request):
    form = CreateCarForm(request.POST or None)
    profile = get_profile()
    if request.method == 'POST':
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = profile
            car.save()
            return redirect('catalogue')

    context = {'form': form, 'profile': profile}

    return render(request, 'cars/car-create.html', context)


class CarFormMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['image_url'].widget.attrs['placeholder'] = 'https://...'

        return form


def car_list(request):
    cars = Car.objects.all()
    profile = get_profile()
    context = {'cars': cars
        , 'profile': profile}

    return render(request, 'cars/catalogue.html', context)


def car_edit(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = CarEditForm(request.POST or None, instance=car)
    profile = get_profile()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'form': form, 'car': car, 'profile': profile}

    return render(request, 'cars/car-edit.html', context)


def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = CarEditForm(request.POST or None, instance=car)
    profile = get_profile()

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    context = {'profile': profile, 'car': car, 'form': form}
    return render(request, 'cars/car-delete.html', context)


def car_details(request, pk):
    car = get_object_or_404(Car, pk=pk)
    profile = get_profile()

    context = {
        'car': car,
        'profile': profile
    }
    return render(request, 'cars/car-details.html', context)
