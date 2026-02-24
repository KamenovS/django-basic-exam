from django.urls import path
from .import views

urlpatterns = [
    path('', views.CompanyListView.as_view(), name='company_list'),
    path('create-company/', views.CompanyCreateView.as_view(), name='company_create'),
    path('<int:pk>/edit-company/', views.CompanyUpdateView.as_view(), name='company_update'),
    path('<int:pk>/delete-company/', views.CompanyDeleteView.as_view(), name='company_delete'),
    path("detail/<int:pk>/", views.CompanyDetailView.as_view(), name='company_detail'),
    path('offer-list', views.OfferListView.as_view(), name='offer_list'),
    path('create/', views.OfferCreateView.as_view(), name='offer_create'),
    path('<int:pk>/edit/', views.OfferUpdateView.as_view(), name='offer_update'),
    path('<int:pk>/delete/', views.OfferDeleteView.as_view(), name='offer_delete'),
]