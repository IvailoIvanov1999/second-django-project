from django.urls import path

from world_of_speed.web.views import home_page

urlpatterns = [
    path('', home_page, name='index')
]
