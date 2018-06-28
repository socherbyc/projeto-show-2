import os
import uuid
from django.dispatch import receiver

from django.db import models
from django.utils import timezone

# Create your models here.

class GVector(models.Model):
    description = models.CharField(max_length=255, blank=True)
    gvector = models.FileField(upload_to='gvector/')
    is_in_queue = models.BooleanField(default=False)
    is_processing = models.BooleanField(default=False)
    percentage = models.FloatField(max_length=255, default=0)
    created_at = models.DateTimeField(default=timezone.now)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    @property
    def percentage_text(self):
        return "{:10.2f}%".format(self.percentage * 100).strip()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "gvectors"

@receiver(models.signals.post_delete, sender=GVector)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.gvector and os.path.isfile(instance.gvector.path):
        os.remove(instance.gvector.path)