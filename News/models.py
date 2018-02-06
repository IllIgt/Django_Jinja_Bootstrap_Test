from django.db import models
from django.utils import timezone


class Authors (models.Model):
    surname = models.CharField(max_length=12)
    initials = models.CharField(max_length=6)
    is_lab_employee = models.BooleanField(default=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.surname + ' ' + self.initials


class Publications(models.Model):
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, default='Unknown')
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

