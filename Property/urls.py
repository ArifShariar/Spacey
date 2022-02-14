from django.urls import path
from . import views

urlpatterns = [
    # TODO: PASS USER ID IN THE URLS TO MAKE DYNAMIC URL ROUTING
    path('host/', views.host, name='host'),
    path('host/success', views.hosting_successful, name='hosting_successful'),

    path('host/personal', views.host_personal_room, name='host_personal_room'),
    path('host/business_storage', views.host_business_storage, name='host_business_storage'),
    path('host/climate_controlled_storage', views.host_climate_controlled_storage,
         name='host_climate_controlled_storage'),
    path('host/garage', views.host_garage, name='host_garage'),
]
