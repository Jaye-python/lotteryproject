from django.contrib import admin

# Register your models here.

from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
  list_display = ('plays', 'rtp', 'created')
  readonly_fields = ('created',)

admin.site.register(Ticket, TicketAdmin)
