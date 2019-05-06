from django.urls import path
from . import views
from django.contrib.auth import views as auth_views   # Class-bassed Views
from users import views as user_views



urlpatterns = [
	# Register
	path('register/', views.Register, name='register'),
    
    # By default template_name = 'registration/login.html' below
    # Login
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    # Logout
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # Profile
    path('profile/', user_views.Profile, name='profile'),
    
]
