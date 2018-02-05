from django.db import models
from django.utils import timezone


class Publications(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    publishing_house = models.TextField()
    date = models.DateField('Дата публикации')
    location = models.CharField(max_length=200)
    pages = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
