from django.urls import path

from .views import UserList, UserDetail, GroupList

app_name = 'authentication'

urlpatterns = [
    path('users/', UserList.as_view(), name='users'),
    path('users/<pk>/', UserDetail.as_view(), name='user-detail'),
    path('groups/', GroupList.as_view(), name='groups'),
]
