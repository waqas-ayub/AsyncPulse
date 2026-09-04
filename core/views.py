from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from celery.result import AsyncResult

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

        # Trigger Celery task
        task = send_webhook_notification.delay(target_url, payload)

        return Response({
            "message": "Webhook task queued successfully",
            "task_id": task.id
        }, status=status.HTTP_202_ACCEPTED)


class TaskStatusView(APIView):
    def get(self, request, task_id):
        task_result = AsyncResult(task_id)
        return Response({
            "task_id": task_id,
            "status": task_result.status,
            "result": task_result.result if task_result.ready() else None
        }, status=status.HTTP_200_OK)


class GenerateReportView(APIView):
    def post(self, request):
        return Response({"message": "Report generation endpoint ready"}, status=status.HTTP_200_OK)