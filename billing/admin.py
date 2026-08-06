from django.contrib import admin
from .models import  Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'service_type', 'status', 'created_at')
    list_filter = ('status', 'service_type', 'created_at')
    search_fields = ('ticket_number', 'service_type')
    list_editable = ('status',) # Talon statusyny (garaşýar, tamamlandy we ş.m.) göni sanawdan üýtgetmek üçin
    readonly_fields = ('created_at',) # Döredilen wagty üýtgedip bolmaz ýaly