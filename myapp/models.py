from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    post_title = models.CharField(max_length=100)
    post_content = models.TextField()
    post_image = models.ImageField(upload_to='posts/')
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title