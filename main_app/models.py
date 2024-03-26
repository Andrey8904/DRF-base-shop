from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=250)
    create = models.DateTimeField(auto_now_add=True)
