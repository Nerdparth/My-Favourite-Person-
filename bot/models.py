from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class BotInforamtion(models.Model):  #BotInforamtion
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),]
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    age=models.IntegerField(null=False, blank=False)
    gender=models.CharField(null=False, blank=False, max_length=1, choices=GENDER_CHOICES, default='F')
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='media\images',null=True,blank=True)
    chat_file = models.FileField(blank=True,null=True,upload_to="media/chats")
    botdescription = models.CharField(max_length=255, blank=True, null=True, default="my favourite person")

    def __str__(self):
        return self.user.username + str(self.uuid)
    

class ChatDescription(models.Model):
    image = models.ImageField(upload_to='media\images',null=True,blank=True)
    # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chat_file = models.FileField(blank=True,null=True,upload_to="media/chats")
    botdescription = models.CharField(max_length=255, blank=False, null=False, default="My favourite person")


    
    def __str__(self):
        return self.user.username + str(self.uuid)
