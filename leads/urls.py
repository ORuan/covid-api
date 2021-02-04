from django.urls import path
from views import register_users, cancel_users

urlpatterns = [
    path('create/', register_users, name="create"),
    path('cancel/', cancel_users, name="cancel"),
    path('sucess/', register_users, name="sucess"),
]