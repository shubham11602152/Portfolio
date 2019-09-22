from django.db import models

# Create your models here.

# categories of posts.


class Category(models.Model):
    name = models.CharField(max_length=20)

# post.


class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('category', related_name='posts')


# comment


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
