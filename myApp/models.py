from django.db import models

class UserProfile(models.Model):
    user_id = models.CharField(max_length=255)  # Firebase UID
    display_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
