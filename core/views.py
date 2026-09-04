from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from celery.result import AsyncResult

from .serializers import UserRegisterSerializer
from .tasks import send_welcome_email_task, generate_user_report_task

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_welcome_email_task.delay(user.email)
            return Response(
                {"message": "User registered successfully! Welcome email queued."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GenerateReportView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        task = generate_user_report_task.delay(user_id)
        return Response(
            {
                "message": "Report generation started in background.",
                "task_id": task.id
            },
            status=status.HTTP_202_ACCEPTED
        )

class TaskStatusView(APIView):
    def get(self, request, task_id):
        task_result = AsyncResult(task_id)
        
        response_data = {
            "task_id": task_id,
            "status": task_result.status,  # PENDING, STARTED, SUCCESS, FAILURE
            "result": task_result.result if task_result.ready() else None
        }
        
        return Response(response_data, status=status.HTTP_200_OK)