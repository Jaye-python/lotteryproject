from rest_framework import serializers
from lotapp.models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'plays', 'rtp']