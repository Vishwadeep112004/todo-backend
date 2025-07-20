from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    task=serializers.CharField(max_length=50)
    status=serializers.BooleanField(default=False)

    def create(self, data):
        return Task.objects.create(**data)
    
    def update(self, instance, data):
        instance.id=data.get('id', instance.id)
        instance.task=data.get('task', instance.task)
        instance.status=data.get('status', instance.status)
        instance.save()
        return instance