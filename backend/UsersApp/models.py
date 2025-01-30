from django.db import models
from django.contrib.auth.models import User
from RoomApp.models import Room
class Profile(models.Model):
    ROLE_CHOICES = [
        ('USER', 'User'),
        ('HOUSEKEEPER', 'Housekeeper'),
        ('MANAGER', 'Manager'),
        ('RECEPTIONIST', 'Receptionist'),
        ('DEVELOPER','Developer'),
    ]
    #legatura de one to one cu tabela de user , models.CASCADE reprezinta faptul ca , daca userul cu care este legat profilul se sterge
    # automat se va sterge si profilul legat, blank-false null=false rezulta faptul ca nu putem crea o variabila de tip Profile fara un user(blank=false)
    # dar nu putem nici sa salvam o variabila de tip Profile in database fara user (null=false)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    #image este un path catre folderul de imagini al serverului , e configurata deja de dinainte de catre FRAMEWORK
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    #role va putea fi doar una din optiunile selectate in ROLE_CHOICES
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='USER')
    
    def __str__(self):
        return self.user.email

class UserRegistrationRequest(models.Model):
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    role = models.CharField(choices = Profile.ROLE_CHOICES, max_length=100)
    
    def __str__(self):
        return self.email
class Booking(models.Model):
    CHOICES = [
        ('PENDING','Pending'),
        ('APPROVED','Approved'),
        ('REJECTED','Rejected')
    ]
    room = models.OneToOneField(Room,on_delete=models.CASCADE,default=1)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    cost = models.FloatField(null=False,blank=False,default=0.0)
    status = models.CharField(max_length=10, choices=CHOICES, default='PENDING')


class Task(models.Model):
    user = models.ForeignKey(User,blank=False,null=False,on_delete=models.CASCADE)
    room = models.OneToOneField(Room,blank=False,null=False,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=False,null=False)
    description = models.TextField(blank=True,null=True)
    