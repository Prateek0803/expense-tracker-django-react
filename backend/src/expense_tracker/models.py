from django.db import models

# Create your models here.
from django.db import models

class Expenses(models.Model):
    amount = models.IntegerField()
    title = models.CharField(max_length = 30)
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length = 30)
    sub_category = models.CharField(max_length = 30)
    payment = models.CharField(max_length = 30)

    def __str__(self):
        return self.title