
from django.contrib import admin
from django.urls import path
from clients.views import ClientListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clients/', ClientListView.as_view())
]
