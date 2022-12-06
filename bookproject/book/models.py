from django.db import models 


class Book(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    
# Book.objects.order_by( '-id' )
# Reserved.objects.all().filter(client=client_id).order_by('check_in') 
# Data.objects.order_by('date').reverse().first()

# Create your models here.

