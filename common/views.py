from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, DetailView

from common.forms import AvailabilityCommentForm, OfferCommentForm
from common.mixins import BackgroundImageMixin
from companies.models import Offer
from drivers.models import DriverAvailability


class HomeView(BackgroundImageMixin, TemplateView):
    template_name = 'common/home.html'
    paginate_by = 3
    bg_image = 'images/home_bg.jpg'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_query = self.request.GET.get('q', '').strip()

        offers_qs = Offer.objects.all()
        if search_query:
            offers_qs = offers_qs.filter(
                Q(pickup_location__icontains=search_query) |
                Q(delivery_location__icontains=search_query)
            )
        offers_qs = offers_qs.order_by('-created_at')

        drivers_qs = DriverAvailability.objects.all()
        if search_query:
            drivers_qs = drivers_qs.filter(
                current_location__icontains=search_query
            )
        drivers_qs = drivers_qs.order_by('-created_at')

        offers_page_obj = Paginator(offers_qs, self.paginate_by).get_page(
            self.request.GET.get('offers_page')
        )
        drivers_page_obj = Paginator(drivers_qs, self.paginate_by).get_page(
            self.request.GET.get('drivers_page')
        )

        context.update({
            'offers_page_obj': offers_page_obj,
            'drivers_page_obj': drivers_page_obj,
            'search_query': search_query,
        })

        return context


class OfferDetailView(BackgroundImageMixin, DetailView):
    model = Offer
    template_name = 'common/offer_detail.html'
    context_object_name = 'offer'
    bg_image = 'images/company_bg.jpg'

    def get_queryset(self):
        return Offer.objects.prefetch_related('drivers', 'comments')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        comments_list = self.object.comments.all().order_by('-created_at')
        paginator = Paginator(comments_list, 2)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        context['comments'] = page_obj.object_list
        context['drivers'] = self.object.drivers.all()
        context['form'] = OfferCommentForm()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = OfferCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.offer = self.object
            comment.save()

            self.object.drivers.add(comment.driver)

            return redirect(
                reverse('offer_detail', kwargs={'pk': self.object.pk})
            )

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


class AvailabilityDetailView(BackgroundImageMixin, DetailView):
    model = DriverAvailability
    template_name = 'common/availability_detail.html'
    context_object_name = 'availability'
    bg_image = 'images/driver_bg.jpg'

    def get_queryset(self):
        return DriverAvailability.objects.prefetch_related('companies', 'comments')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        comments_list = self.object.comments.all().order_by('-created_at')
        paginator = Paginator(comments_list, 2)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        context['comments'] = page_obj.object_list
        context['companies'] = self.object.companies.all()
        context['form'] = AvailabilityCommentForm()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = AvailabilityCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.availability = self.object
            comment.save()

            self.object.companies.add(comment.company)

            return redirect(
                reverse('availability_detail', kwargs={'pk': self.object.pk})
            )

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)