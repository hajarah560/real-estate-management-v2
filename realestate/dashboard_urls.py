from django.urls import path
from management.dashboard_view import dashboard
from .urls import urlpatterns as existing_patterns

urlpatterns = [
    path('', dashboard, name='dashboard_home'),
    path('dashboard/', dashboard, name='dashboard'),
] + existing_patterns
