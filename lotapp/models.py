from django.db import models

# Create your models here.
class Ticket(models.Model):
    plays = models.JSONField()
    rtp = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)