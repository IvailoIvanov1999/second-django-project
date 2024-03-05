from django.urls import path

from world_of_speed.profiles.views import create_profile, profile_details, profile_edit, profile_delete

urlpatterns = [
    path('create/', create_profile, name='profile-create'),
    path('details/', profile_details, name='profile-details'),
    path('edit/', profile_edit, name='profile-edit'),
    path('delete/', profile_delete, name='profile-delete')
]
