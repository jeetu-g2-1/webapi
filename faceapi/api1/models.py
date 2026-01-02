from django.db import models

# Create your models here.

class APIKey(models.Model):
    name=models.CharField(max_length=100)
    hashed_key=models.CharField(max_length=128, unique=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)




class FaceImageResponse(models.Model):
    original_img_response = models.TextField()
    face_img_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class APIRequestLog(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)

    content_type = models.CharField(max_length=100, null=True, blank=True)
    content_length = models.IntegerField(null=True, blank=True)

    headers = models.JSONField()
    body = models.TextField(blank=True)

    parsed_data = models.JSONField(null=True, blank=True)
    files_count = models.IntegerField(default=0)

    user_agent = models.TextField(blank=True)
    status_code = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.method} {self.path} ({self.created_at})"

