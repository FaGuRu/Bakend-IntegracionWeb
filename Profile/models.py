from django.db import models
from django.contrib.auth.models import User

class ProfileModel(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET(-1))
    address = models.CharField(max_length = 255, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.user

class ProfileTwo(models.Model):
    profileModel = models.ForeignKey(ProfileModel, on_delete = models.SET(-1))
    address = models.CharField(max_length = 255, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.profileModel

##-----------------------------------------------Tabla de usuarios que se vizualizara en Front-----------------------------------------------------

class Users(models.Model):
    fullname = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    age = models.IntegerField()

    def __str__(self):
        return self.fullname


#---------------------------------------------------------Metodos Get, Put y Delete-------------------------------------------------------------------

#Create/Insert/Add - Post

#Retrieve/ Fetch - Get

#Update/Edit - Put

#Delete/ Remove - Delete
