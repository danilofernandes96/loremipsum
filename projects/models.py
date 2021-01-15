from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Project(models.Model):
    OPTIONS = (
        (0, 'baixo'),
        (1, 'medio'),
        (2, 'alto'),
    )
    name = models.CharField('Nome do projeto', max_length=255)
    startData = models.DateField('Data de início', blank=False, auto_now=False)
    endData = models.DateField('Data de término', auto_now=False)
    risk = models.IntegerField(
        'Risco',choices=OPTIONS,
    )
    price = models.DecimalField('Valor',max_digits=10, decimal_places=2)
    stakeholders = models.CharField('Participantes', max_length=500, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
