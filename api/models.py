from django.core.validators import MinLengthValidator, EmailValidator
from django.db import models
import datetime

from django.contrib.auth.models import User, Group

LEVEL_CHOICES = [
    ('critical', 'critical'),
    ('debug', 'debug'),
    ('error', 'error'),
    ('warning', 'warning'),
    ('information', 'info'),
]


class Agent(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    address = models.URLField(null=True)
    status = models.BooleanField(default=False)
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Event(models.Model):
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500)
    agent = models.ForeignKey(Agent, on_delete=models.PROTECT)
    arquivado = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.level + ' in ' + self.agent.name

    class Meta:
        ordering = ['date']
