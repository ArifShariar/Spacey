from django.urls import path
from . import views

urlpatterns = [
    # TODO: PASS USER ID IN THE URLS TO MAKE DYNAMIC URL ROUTING
    path('<str:pk>/host', views.host, name='host'),
    path('<str:pk>/host/success', views.hosting_successful, name='hosting_successful'),
    path('<str:pk>/host/addPhoto', views.addPhoto, name='addPhoto'),
    path('<str:pk>/host/personal', views.host_personal_room, name='host_personal_room'),
    path('<str:pk>/host/business_storage', views.host_business_storage, name='host_business_storage'),
    path('<str:pk>/host/climate_controlled_storage', views.host_climate_controlled_storage,
         name='host_climate_controlled_storage'),
    path('<str:pk>/host/garage', views.host_garage, name='host_garage'),
]
