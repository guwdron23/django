from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(blank=True, null=True, verbose_name='Текст')
    count_like = models.PositiveIntegerField(default=0, verbose_name='Лайк')
    create_at = models.DateTimeField(auto_created=True, verbose_name='Дата создание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_post')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['count_like']


class Comment(models.Model):
    post: Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    count_likes = models.PositiveIntegerField(default=0, verbose_name='Лайк')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment')

    def __str__(self):
        return self.post.title + ' ' + self.text