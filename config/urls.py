from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from core.views import RegisterView, GenerateReportView, TaskStatusView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Auth Endpoints
    path('api/auth/register/', RegisterView.as_view(), name='auth_register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Background Async Endpoints
    path('api/reports/generate/', GenerateReportView.as_view(), name='generate_report'),
    
    # Task Tracking Endpoint
    path('api/tasks/<str:task_id>/', TaskStatusView.as_view(), name='task_status'),
]