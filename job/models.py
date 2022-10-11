from random import choices
from django.db import models
import datetime
# Create your models here.

job_type_choices = (('Full Time', 'Full Time'),
                    ('Part Time', 'Part Time'),
                    )
gander_choices = (('Male', 'Male'),('Female', 'Female'),('Prefer to not respons', 'Prefer to not respons'))

class job(models.Model):
    title = models.CharField(max_length=100)
    #location
    jop_type = models.CharField(max_length=20, choices=job_type_choices, default=None)
    description = models.TextField(max_length=1500, default=None)
    published_date = models.DateField(auto_now_add=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    gander = models.CharField(max_length=30, choices=gander_choices, default=None, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title

class category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.name