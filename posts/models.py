from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=75, unique=True)
    body = models.TextField(blank=True)
    excerpt = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    comments = GenericRelation(Comment)

    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title}, {self.author}"
    
    def get_content_type_id(self):
        return ContentType.objects.get_for_model(self.__class__).id