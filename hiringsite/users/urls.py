from django.urls import path
from .views import users_index, UserLoginView, \
UserRegister, user_profile, UserLogoutView, ProfileUpdateView

urlpatterns = [
    path('', users_index, name='user'),
    path('profile/<int:pk>/update/', ProfileUpdateView.as_view(), name='update'),
    path('profile/<id>', user_profile, name='profile'),
    path('login', UserLoginView.as_view(), name='login'),
    path('register', UserRegister.as_view(), name='register'),
    path('logout', UserLogoutView.as_view(), name='logout'),

]
