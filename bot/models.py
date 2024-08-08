from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class bot_information(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100, null=False, blank=False)
    age=models.IntegerField(null=False, blank=False)
    # image = models.ImageField(upload_to='media\images')
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)