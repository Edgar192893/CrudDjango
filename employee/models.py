from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length= 100)
    email = models.EmailField()
    contacto = models.CharField(max_length=13)


    def __str__(self):
        return "%s" %(self.name)
    
    class Meta:
        db_table = "employee"