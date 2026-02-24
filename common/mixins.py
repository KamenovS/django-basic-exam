from django.db import models
from django.templatetags.static import static

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class BackgroundImageMixin:
    bg_image = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.bg_image:
            context['bg_image_url'] = static(self.bg_image)
        return context