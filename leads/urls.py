from leads.views import register_users, cancel_users
from django.urls import path, include


urlpatterns = [
    path('create/', register_users, name="create"),
    path('cancel/', cancel_users, name="cancel"),
]
