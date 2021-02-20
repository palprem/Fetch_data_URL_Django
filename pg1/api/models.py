  
from django.db import models

class DATA(models.Model):
    title = models.CharField(max_length=150)
    # date = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
    int_grp = models.CharField(max_length=100)
    def __str__(self):
        return self.title