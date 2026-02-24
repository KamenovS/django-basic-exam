from common.mixins import BackgroundImageMixin
from .choices import DriverCategoryChoices, TrailerTypeChoices
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import DriverAvailability
from .forms import DriverAvailabilityForm
from django.db.models import Q
from .models import Driver
from .forms import DriverForm


class DriverListView(BackgroundImageMixin , ListView):
    model = Driver
    template_name = 'driver/driver_list.html'
    context_object_name = 'drivers'
    paginate_by = 6
    bg_image = 'images/driver_bg.jpg'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', '').strip().upper()

        if search_query:
            category_values = [
                key for key, display in DriverCategoryChoices.choices
                if search_query in display.upper()
            ]

            trailer_values = [
                key for key, display in TrailerTypeChoices.choices
                if search_query in display.upper()
            ]

            queryset = queryset.filter(
                Q(category__in=category_values) |
                Q(trailer_type__in=trailer_values)
            )

        return queryset


class DriverBaseFormView(BackgroundImageMixin):
    model = Driver
    form_class = DriverForm
    template_name = 'driver/driver_form.html'
    success_url = reverse_lazy('driver_list')
    bg_image = 'images/driver_bg.jpg'


class DriverCreateView(DriverBaseFormView, CreateView):
    pass


class DriverUpdateView(DriverBaseFormView, UpdateView):
    pass


class DriverDeleteView(BackgroundImageMixin , DeleteView):
    model = Driver
    template_name = 'driver/driver_confirm_delete.html'
    success_url = reverse_lazy('driver_list')
    bg_image = 'images/driver_bg.jpg'


class DriverDetailView(BackgroundImageMixin , DetailView):
    model = Driver
    template_name = 'driver/driver_detail.html'
    context_object_name = 'driver'
    bg_image = 'images/driver_bg.jpg'


class AvailabilityListView(BackgroundImageMixin, ListView):
    model = DriverAvailability
    template_name = 'availability/availability_list.html'
    context_object_name = 'availabilities'
    paginate_by = 6
    bg_image = 'images/driver_bg.jpg'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        location = self.request.GET.get('location')
        if location:
            queryset = queryset.filter(current_location__icontains=location)
        return queryset


class AvailabilityBaseFormView(BackgroundImageMixin):
    model = DriverAvailability
    form_class = DriverAvailabilityForm
    template_name = 'availability/availability_form.html'
    success_url = reverse_lazy('availability_list')
    bg_image = 'images/driver_bg.jpg'


class AvailabilityCreateView(AvailabilityBaseFormView, CreateView):
    pass


class AvailabilityUpdateView(AvailabilityBaseFormView, UpdateView):
    pass


class AvailabilityDeleteView(BackgroundImageMixin, DeleteView):
    model = DriverAvailability
    template_name = 'availability/availability_confirm_delete.html'
    success_url = reverse_lazy('availability_list')
    bg_image = 'images/driver_bg.jpg'





