from leads.views import register_users, cancel_users, sucess
from django.urls import path, include


urlpatterns = [
    path('create/', register_users, name="create"),
    path('sucess/',sucess , name="sucess"),
    path('cancel/', cancel_users, name="cancel"),
]