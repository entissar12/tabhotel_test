from rest_framework import viewsets
from .serializers import TicketSerializer
from .models import Ticket
from django_filters.rest_framework import DjangoFilterBackend


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sender',]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
