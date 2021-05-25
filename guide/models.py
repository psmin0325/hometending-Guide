from django.db import models

class baseAlchohol(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length = 10)

class supportAlchohol(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length = 10)

class additives(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length = 10)

class result(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length = 10)
    desc = models.TextField()

