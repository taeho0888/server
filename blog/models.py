from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    contents = models.CharField(max_length=100)