from rest_framework import serializers


class AssignTaskRequest(serializers.Serializer):
    user = serializers.CharField()
    room = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    status = serializers.CharField()
    
class UpdateTaskToInProgress(serializers.Serializer):
    task_id = serializers.CharField()
    
class UpdateTaskToInDone(UpdateTaskToInProgress):
    pass