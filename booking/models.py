from django.db import models


class ServiceOffering(models.Model):

    title= models.CharField(max_length=120)
    description = models.TextField(blank=True)

    duration_minutes = models.PositiveIntegerField()

    price = models.PositiveIntegerField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

