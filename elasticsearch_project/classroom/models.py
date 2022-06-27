from msilib.schema import Class
from django.db import models
from django.utils import timezone

# Create your models here.
class Classroom(models.Model):
    class_name = models.CharField(max_length=150)
    class_description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'classrooms'

    def __str__(self):
        return self.class_name
