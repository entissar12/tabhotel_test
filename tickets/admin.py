from django.contrib import admin
from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'sender', 'status', 'category', 'date']

admin.site.register(Ticket, TicketAdmin)
