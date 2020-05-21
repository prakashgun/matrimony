from django.urls import path

from .views import UserList, GroupList

app_name = 'authentication'

urlpatterns = [
    path('users/', UserList.as_view(), name='users'),
    path('groups/', GroupList.as_view(), name='groups'),
]
