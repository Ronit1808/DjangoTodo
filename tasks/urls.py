from django.urls import path
from .views import CreateTaskView, AssignTaskView, UserTasksView, home

urlpatterns = [
    path('', home, name='home'),
    path('tasks/create/', CreateTaskView.as_view(), name='create-task'),
    path('tasks/<int:task_id>/assign/', AssignTaskView.as_view(), name='assign-task'),
    path('tasks/user/<int:user_id>/', UserTasksView.as_view(), name='user-tasks'),
]
