from django.shortcuts import render
from .models import User, Task, Room 
from UsersApp.models import Profile
from rest_framework.decorators import APIView
from drf_yasg.utils import swagger_auto_schema
from .requests import AssignTaskRequest, UpdateTaskToInProgress , UpdateTaskToInDone
from rest_framework.response import Response
from rest_framework import status
from .serializer import TaskSerializer



class AssignTaskView(APIView):
    @swagger_auto_schema(request_body=AssignTaskRequest)
    def post(self,request,user_accessing_pk):
        try:
            user_requesting_creation = User.objects.get(id=user_accessing_pk)
            profile_for_user_requesting_creation = Profile.objects.get(user=user_requesting_creation)
            if profile_for_user_requesting_creation.role != "RECEPTIONIST":
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            user = User.objects.get(id=request.data.get("user"))
            room = Room.objects.get(id=request.data.get("room"))
            Task.objects.create(user=user,room=room,name=request.data.get("name"),description=request.data.get("description"),status="PENDING")
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    @swagger_auto_schema(request_body=UpdateTaskToInProgress)
    def put(self,request,user_accessing_pk):
        try:
            user_requesting_creation = User.objects.get(id=user_accessing_pk)
            profile_for_user_requesting_creation = Profile.objects.get(user=user_requesting_creation)
            if profile_for_user_requesting_creation.role != "HOUSEKEEPER":
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            task = Task.objects.get(id=request.data.get("task_id"))
            task.status = "IN_PROGRESS"
            task.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        
    def get(self,request,user_accessing_pk):
         try:
            user_requesting_get = User.objects.get(id=user_accessing_pk)
            profile_for_user_requesting_get = Profile.objects.get(user=user_requesting_get)
            if profile_for_user_requesting_get.role == "HOUSEKEEPER" :  
                tasks = Task.objects.filter(user=user_requesting_get)
                serialized_data = TaskSerializer(tasks,many=True)
                return Response(serialized_data.data,status=status.HTTP_200_OK)
            elif profile_for_user_requesting_get.role == "RECEPTIONIST":
                tasks = Task.objects.all()
                serialized_data = TaskSerializer(tasks,many=True)
                return Response(serialized_data.data,status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
         except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from rest_framework.decorators import api_view
@api_view(['DELETE'])
def deleteTask(request,user_accessing_pk,task_id):
        try:
            user_requesting_creation = User.objects.get(id=user_accessing_pk)
            profile_for_user_requesting_creation = Profile.objects.get(user=user_requesting_creation)
            if profile_for_user_requesting_creation.role != "HOUSEKEEPER" and profile_for_user_requesting_creation.role != "RECEPTIONIST":
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            task = Task.objects.get(id=task_id)
            task.status = "DONE"
            task.save()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)