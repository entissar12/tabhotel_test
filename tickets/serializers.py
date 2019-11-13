from rest_framework import serializers
from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'title', 'description', 'image', 'sender', 'status', 'date', 'category']
