from django.db import models

class Leads(models.Model):
    number = models.CharField(max_length=15, null=False)
    city = models.CharField(max_length=50, null=False)