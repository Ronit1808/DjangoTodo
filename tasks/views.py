
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Task, User
from .serializers import TaskSerializer, TaskAssignSerializer
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the Task API!"})

# Create Task API
class CreateTaskView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Assign Task API
class AssignTaskView(APIView):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        serializer = TaskAssignSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Task assigned successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get Tasks for User API
class UserTasksView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        tasks = user.tasks.all()  # Get all tasks assigned to the user
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
