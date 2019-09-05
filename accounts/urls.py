from django.urls import path
from .views import RegisterView, LoginView, ProfileView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='accounts-register'),
    path('login/', LoginView.as_view(), name='accounts-login'),
    path('profile/', ProfileView.as_view(), name='accounts-profile'),
    path('logout/', LogoutView.as_view(), name='accounts-logout'),
]