from rest_framework import routers
from .views import TicketViewSet

router = routers.DefaultRouter()
router.register(r'tickets', TicketViewSet)
