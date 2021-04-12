from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from rest_framework.routers import SimpleRouter

# router = SimpleRouter()
# router.register(r'users', UserProfileApiView)


urlpatterns = [
    path('users/', UsersListView.as_view(), name='users_list'),
    path('users/delete/<int:pk>/', user_delete, name='delete'),
    # path('users/delete/', DeleteUserView.as_view(), name = 'delete_users'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = '/'), name = 'logout'),
    path('registrations/', RegisterView.as_view(), name = 'register'),
]

