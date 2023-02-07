from django.urls import path
from . views import *

urlpatterns = [
    path('generate/', GenerateRandomUserView.as_view(), name="generate"),
    path('', UsersListView.as_view(), name="users_list"),
]
