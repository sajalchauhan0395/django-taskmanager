from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from rest_framework import viewsets
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

#List Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html',{'tasks': tasks})

#Add Task

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html',{'form':form})

#Edit Task

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'form':form})

#Delete task

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    
    return render(request, 'tasks/task_confirm_delete.html',{'task':task})

#API View

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List':'/api/task-list',
        'Detail View' : '/api/task-detail/<int:id>',
        'Create' : '/api/task-create',
        'Update' : '/api/task-update/<int:id>',
        'Delete' :'/api/task-delete/<int:id',
        }
    return Response(api_urls)

@api_view(['GET'])
def task_list_api(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def task_detail_api(request):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def task_create_api(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def task_update_api(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def task_delete_api(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return Response('Task deleted successfully')

# Create your views here.
