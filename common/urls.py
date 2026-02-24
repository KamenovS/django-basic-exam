from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('companies/<int:pk>/', views.OfferDetailView.as_view(), name='offer_detail'),
    path('drivers/<int:pk>/', views.AvailabilityDetailView.as_view(), name='availability_detail'),
]
