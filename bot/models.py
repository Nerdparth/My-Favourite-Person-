from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class bot_information(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')]
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age=models.IntegerField(null=False, blank=False)
    gender=models.CharField(null=False, blank=False, max_length=6, choices=GENDER_CHOICES, default='male')

    # image = models.ImageField(upload_to='media\images')
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)