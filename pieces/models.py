from django.db import models

# Create your models here.
class Piece(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Conductor(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null = True)
    last_name = models.CharField(max_length=200)
    prefix = models.CharField(max_length=20, null = True)
    suffix = models.CharField(max_length=20, null = True)

class Performance(models.Model):
    piece = models.ForeignKey(Piece)
    conductor = models.ForeignKey(Conductor)
    date = models.DateTimeField('date performed')

    
    
