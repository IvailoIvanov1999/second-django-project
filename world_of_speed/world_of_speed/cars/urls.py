from django.urls import path, include

from world_of_speed.cars.views import car_list, create_car, car_details, car_edit, car_delete

urlpatterns = [
    path('catalogue/', car_list, name='catalogue'),
    path('create/', create_car, name='car-create'),
    path('<int:pk>/', include([
        path('details/', car_details, name='car-details'),
        path('edit/', car_edit, name='car-edit'),
        path('delete/', car_delete, name='car-delete')
    ]))
]
