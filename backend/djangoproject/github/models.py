from django.db import models
from django.conf import settings

class GitHubAccount(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)  # Optional field to store GitHub username

    def __str__(self):
        return f"{self.user.username}'s GitHub Account"
