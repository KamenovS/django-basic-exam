from django.urls import path
from . import views

urlpatterns = [
    path('', views.DriverListView.as_view(), name='driver_list'),
    path('create-driver/', views.DriverCreateView.as_view(), name='driver_create'),
    path('<int:pk>/edit-driver/', views.DriverUpdateView.as_view(), name='driver_update'),
    path('<int:pk>/delete-driver/', views.DriverDeleteView.as_view(), name='driver_delete'),
    path('detail/<int:pk>/', views.DriverDetailView.as_view(), name='driver_detail'),
    path('availability-list/', views.AvailabilityListView.as_view(), name='availability_list'),
    path('create-availability/', views.AvailabilityCreateView.as_view(), name='availability_create'),
    path('<int:pk>/edit/', views.AvailabilityUpdateView.as_view(), name='availability_update'),
    path('<int:pk>/delete/', views.AvailabilityDeleteView.as_view(), name='availability_delete'),
]
