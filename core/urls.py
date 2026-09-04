from django.urls import path
from .views import RegisterView, GenerateReportView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('reports/generate/', GenerateReportView.as_view(), name='generate-report'),
]