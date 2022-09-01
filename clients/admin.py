from django.contrib import admin
from clients.models import Client

class Clients(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'country', 'city']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'country']
    list_per_page = 20
    

admin.site.register(Client, Clients)
