from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Contact(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    relevante = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numero = models.CharField(max_length=15, blank=True, null=True)



    def __str__(self):
        return f"{self.nombre} - by {self.user.username}" 
    
    