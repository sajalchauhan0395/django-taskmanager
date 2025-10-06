from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/tasks',views.TaskViewSet)

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:pk>/', views.edit_task, name = 'edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('',include(router.urls),),
    path('api/', views.api_overview, name='api_overview'),
    path('api/task-list/', views.task_list_api, name='task_list_api'),
    path('api/task-detail/<int:id>/', views.task_detail_api, name='task_detail_api'),
    path('api/task-create/', views.task_create_api, name='task_create_api'),
    path('api/task-update/<int:id>/', views.task_update_api, name='task_update_api'),
    path('api/task-delete/<int:id>/', views.task_delete_api, name='task_delete_api'),
]