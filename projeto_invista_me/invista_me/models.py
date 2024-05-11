from django.db import models
from datetime import datetime
# Create your models here.

class Investimentos(models.Model):
    Investimento = models.TextField(max_length=255)
    Valor = models.FloatField()   
    Pago  = models.BooleanField(default=False)    
    Data  = models.DateField(default=datetime.now)
    
    