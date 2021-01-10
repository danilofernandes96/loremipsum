from django.db import models
from django.db.models.enums import Choices

# Create your models here.
class Project(models.Model):
    OPTIONS = (
        (0, 'baixo'),
        (1, 'medio'),
        (2, 'alto'),
    )
    name = models.CharField(max_length=255)
    startData = models.DateField(auto_now=False)
    endData = models.DateField(auto_now=False)
    risk = models.IntegerField(
        choices=OPTIONS,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stakeholders = models.CharField(max_length=500, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
