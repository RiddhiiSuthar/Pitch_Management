from django.db import models


class Pitch(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    last_maintenance_date = models.DateTimeField()
    next_maintenance_date = models.DateTimeField()
    current_condition = models.IntegerField()
    weather = models.CharField(blank=True, null=True, max_length=255)

    TURF_CHOICES = (
        ("natural", "Natural"),
        ("artificial", "Artificial"),
        ("hybrid", "Hybrid"),
    )
    turf_type = models.CharField(
        blank=True, null=True, max_length=10, db_index=True, choices=TURF_CHOICES
    )
