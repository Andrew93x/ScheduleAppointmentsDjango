from django.db import models
from django.contrib.auth.models import User
import json

from django.http import request
from rest_framework.serializers import Serializer

# Create your models here.
class RolesUsers(models.Model):
    roles_type = (
        ('doctor', 'Doctor'),
        ('paciente', 'Paciante'),
    )
    users = models.OneToOneField(User,verbose_name = ('User'), on_delete = models.CASCADE)
    rol = models.CharField(choices = roles_type, max_length = 20)

    class Meta:
        verbose_name = ('Role User')
        verbose_name_plural = ('Roles User')

    def __str__(self):
        return self.users.username


class imagen(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return self.title


class CustomSettings(models.Model):
    section = (
        ('SECTION_ONE', 'Secition one'),
        ('SECTION_TWO', 'Section two'),
        ('SECTION_THREE', 'Section three'),
        ('SECTION_FOUR', 'Section four'),
    )
    id_provider = models.SmallIntegerField()
    id_section = models.CharField(choices = section, max_length=100)
    configuraions = models.JSONField()
    photo = models.ImageField()

    class Meta:
        verbose_name = ('Custom Setting')
        verbose_name_plural = ('Custom Setting')
    
    def __str__(self):
        return self.id_section