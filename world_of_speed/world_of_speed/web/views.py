from django.shortcuts import render
from django.views.generic import TemplateView

from world_of_speed.profiles.models import Profile


def get_profile():
    return Profile.objects.first()


def index(request):
    profile = get_profile()

    context = {'profile': profile}

    return render(request, 'base.html', context)


def home_page(request):
    profile = get_profile()
    context = {'profile': profile}

    return render(request, 'web/index.html', context)
