from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    attachments = models.FileField(upload_to='attachments/', blank=True, null=True)

class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title


