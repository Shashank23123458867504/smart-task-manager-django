from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    timezone = models.CharField(max_length=50, default='Asia/Kolkata')
    profile_image = models.ImageField(null=True, blank=True, upload_to='profile_images/')
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints = [models.UniqueConstraint(fields=['user','name'], name = 'unique_user_category')] 
        indexes = [
        models.Index(fields=['user']),
    ] 
        ordering = ['name']

    def __str__(self):
        return self.name

class TaskTable(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    PRIORITY_CHOICES = ((1,"LOW"),(2,"MEDIUM"),(3,"HIGH"),)
    STATUS_CHOICES = ((1,"PENDING"),(2,"IN PROGRESS"),(3,"COMPLETED"),)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    status=models.IntegerField(choices=STATUS_CHOICES)
    due_date=models.DateTimeField(null=True, blank=True)
    is_deleted=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def clean(self):
        if self.due_date:
            if self.due_date < timezone.now():
                raise ValidationError("Due date cannot be in the past")

    class Meta:
        indexes = [
        models.Index(fields=['user']),
        models.Index(fields=['status']),
        models.Index(fields=['due_date']),
        models.Index(fields=['is_deleted']),
    ]
    ordering = ['-created_at']