from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from common.mixins import BackgroundImageMixin
from .models import Offer, Company
from .forms import OfferForm, CompanyForm


class CompanyListView(BackgroundImageMixin, ListView):
    model = Company
    template_name = 'company/company_list.html'
    context_object_name = 'companies'
    paginate_by = 6
    bg_image = 'images/company_bg.jpg'

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        if q:
            return Company.objects.filter(name__icontains=q)
        return Company.objects.all()


class CompanyBaseFormView(BackgroundImageMixin):
    model = Company
    form_class = CompanyForm
    template_name = 'company/company_form.html'
    success_url = reverse_lazy('company_list')
    bg_image = 'images/company_bg.jpg'


class CompanyCreateView(CompanyBaseFormView, CreateView):
    pass


class CompanyUpdateView(CompanyBaseFormView, UpdateView):
    pass


class CompanyDeleteView(BackgroundImageMixin, DeleteView):
    model = Company
    template_name = 'company/company_confirm_delete.html'
    success_url = reverse_lazy('company_list')
    bg_image = 'images/company_bg.jpg'


class CompanyDetailView(BackgroundImageMixin, DetailView):
    model = Company
    template_name = 'company/company_detail.html'
    context_object_name = 'company'
    bg_image = 'images/company_bg.jpg'


class OfferListView(BackgroundImageMixin, ListView):
    model = Offer
    template_name = 'offer/offer_list.html'
    context_object_name = 'offers'
    paginate_by = 6
    bg_image = 'images/company_bg.jpg'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', '')
        if search_query:
            queryset = queryset.filter(
                Q(pickup_location__icontains=search_query) |
                Q(delivery_location__icontains=search_query)
            )
        return queryset


class OfferBaseFormView(BackgroundImageMixin):
    model = Offer
    form_class = OfferForm
    template_name = 'offer/offer_form.html'  # same template for both
    success_url = reverse_lazy('offer_list')
    bg_image = 'images/company_bg.jpg'


class OfferCreateView(OfferBaseFormView, CreateView):
    pass


class OfferUpdateView(OfferBaseFormView, UpdateView):
    pass


class OfferDeleteView(BackgroundImageMixin, DeleteView):
    model = Offer
    template_name = 'offer/offer_confirm_delete.html'
    success_url = reverse_lazy('offer_list')
    bg_image = 'images/company_bg.jpg'

