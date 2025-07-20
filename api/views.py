from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import io
from .models import Task
from .serializers import TaskSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser


@csrf_exempt
def get(req):
    if req.method == 'GET':
        data = JSONParser().parse(io.BytesIO(req.body)) if req.body else {}
        id = data.get('id', None)
        if id is not None:
            try:
                task = Task.objects.get(id=id)
                ser = TaskSerializer(task)
                return JsonResponse(ser.data)
            except Task.DoesNotExist:
                return JsonResponse({'msg': 'Task not found'}, status=404)
        tasks = Task.objects.all()
        ser = TaskSerializer(tasks, many=True)
        return JsonResponse(ser.data, safe=False)
    return JsonResponse({'msg': 'Only GET request allowed'})


@csrf_exempt
def post(req):
    if req.method == 'POST':
        data = JSONParser().parse(io.BytesIO(req.body))
        ser = TaskSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse({'msg': 'Data inserted successfully'})
        return JsonResponse(ser.errors, status=400)
    return JsonResponse({'msg': 'Only POST request allowed'})


@csrf_exempt
def delete(req):
    if req.method == 'DELETE':
        data = JSONParser().parse(io.BytesIO(req.body))
        id = data.get('id', None)
        if id is not None:
            try:
                task = Task.objects.get(id=id)
                task.delete()
                return JsonResponse({'msg': 'Task deleted successfully'})
            except Task.DoesNotExist:
                return JsonResponse({'msg': 'Task not found'}, status=404)
        return JsonResponse({'msg': 'Invalid id'})
    return JsonResponse({'msg': 'Only DELETE request allowed'})


@csrf_exempt
def update(req):
    if req.method == 'PUT':  
        data = JSONParser().parse(io.BytesIO(req.body))
        id = data.get('id', None)
        if id is not None:
            try:
                task = Task.objects.get(id=id)
                ser = TaskSerializer(task, data=data, partial=True)
                if ser.is_valid():
                    ser.save()
                    return JsonResponse({'msg': 'Data updated successfully'})
                return JsonResponse(ser.errors, status=400)
            except Task.DoesNotExist:
                return JsonResponse({'msg': 'Task not found'}, status=404)
        return JsonResponse({'msg': 'Invalid id'})
    return JsonResponse({'msg': 'Only PUT request allowed'})
