from django.db import models
from django.contrib.auth.models import User 
from RoomApp.models import Room
# Create your models here
class Task(models.Model):
    STATUSES = [
        ("PENDING","Pending"),
        ("IN_PROGRESS","In Progress"),
        ("DONE","Done")
    ]
    user = models.ForeignKey(User,blank=False,null=False,on_delete=models.CASCADE)
    room = models.OneToOneField(Room,blank=False,null=False,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=False,null=False)
    description = models.TextField(blank=True,null=True)
    status = models.CharField(choices=STATUSES,max_length=200)

    def __str__(self):
        return self.name
