from django.db import models
from django.utils import timezone

class Ticket(models.Model):
    """Elektron nobat talonlary"""
    STATUS_CHOICES = (
        ('waiting', 'Garaşýar'),
        ('called', 'Çagyryldy'),
        ('completed', 'Tamamlandy'),
        ('cancelled', 'Ýatyryldy'),
    )

    ticket_number = models.CharField(max_length=20)
    service_type = models.CharField(max_length=100)
    cash_desk = models.CharField(max_length=10, default="1")  # Munuň bardygyny barlap görüň!
    status = models.CharField(max_length=20, default='waiting')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.ticket_number} - {self.service_type} ({self.get_status_display()})"