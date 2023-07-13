from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# для добалвения катергорий, необходимо внести любую из них вручную, УДОбно) на случай изменения контента
class Announcement(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person')
    text = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')
    url = models.URLField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория',
                                 related_name='cats')

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('board:announcement_detail',
                       args=[str(self.id)])


class Comment(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80, verbose_name='Имя')
    email = models.EmailField()
    text = models.TextField(verbose_name="Отклик")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created'])]

    def __str__(self):
        return f"Отклик от {self.name} к {self.announcement}"


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('board:category', args=[self.id])
