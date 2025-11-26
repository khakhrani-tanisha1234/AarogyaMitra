from django.db import models
from django.contrib.auth.models import User

class TherapySchedule(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    therapy_type = models.CharField(max_length=100)
    num_sessions = models.PositiveIntegerField()
    preferred_time = models.CharField(max_length=50)
    priority_level = models.CharField(max_length=20, default='Normal')
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    scheduled_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['scheduled_date', 'preferred_time']  # Sort by date & time

    def __str__(self):
        return f"{self.patient_name} - {self.therapy_type}"
# Create your models here.
