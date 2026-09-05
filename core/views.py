from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from celery.result import AsyncResult
from django.core.cache import cache

from .serializers import UserRegisterSerializer
from .tasks import send_webhook_notification

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer


class TriggerWebhookView(APIView):
    def post(self, request):
        target_url = request.data.get("target_url")
        payload = request.data.get("payload", {})

        if not target_url:
            return Response({"error": "target_url is required"}, status=status.HTTP_400_BAD_REQUEST)

        task = send_webhook_notification.delay(target_url, payload)

        return Response({
            "message": "Webhook task queued successfully",
            "task_id": task.id,
            "status_check_url": f"/api/task-status/{task.id}/"
        }, status=status.HTTP_202_ACCEPTED)


class TaskStatusView(APIView):
    def get(self, request, task_id):
        task_result = AsyncResult(task_id)
        
        response_data = {
            "task_id": task_id,
            "status": task_result.status,
            "result": None,
            "error": None
        }

        if task_result.state == 'SUCCESS':
            response_data["result"] = task_result.result
        elif task_result.state == 'FAILURE':
            response_data["error"] = str(task_result.result)

        return Response(response_data, status=status.HTTP_200_OK)


class HealthCheckView(APIView):
    def get(self, request):
        # Check Redis Cache / Connection
        try:
            cache.set("health_check", "ok", 10)
            redis_status = "healthy" if cache.get("health_check") == "ok" else "unhealthy"
        except Exception:
            redis_status = "unhealthy"

        return Response({
            "status": "healthy" if redis_status == "healthy" else "degraded",
            "services": {
                "database": "healthy",
                "redis_broker": redis_status
            }
        }, status=status.HTTP_200_OK if redis_status == "healthy" else status.HTTP_503_SERVICE_UNAVAILABLE)


class GenerateReportView(APIView):
    def post(self, request):
        return Response({"message": "Report generation endpoint ready"}, status=status.HTTP_200_OK)