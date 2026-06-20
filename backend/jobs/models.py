from django.db import models

# Create your models here.

class Job(models.Model):
    # Only these 4 status values are allowed
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Offer', 'Offer'),
        ('Rejected', 'Rejected'),
    ]

    company = models.CharField(max_length=100)        #Company name
    role = models.CharField(max_length=100)             #Job title
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')
    apply_date = models.DateField()                      #Date you applied
    link = models.URLField(blank=True, null=True)        #Job posting link (optional)
    notes = models.TextField(blank=True, null=True)      #Extra notes (optional)

    def __str__(self):
        return f"{self.role} at {self.company}"          #Shows nicely in Django admin