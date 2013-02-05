from django.db import models

# Create your models here.
class Composer(models.Model):   
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null = True, blank = True)
    last_name = models.CharField(max_length=200)
    prefix = models.CharField(max_length=20, null = True, blank = True)
    suffix = models.CharField(max_length=20, null = True, blank = True)

    def name(self):
        return ("%s %s" % (self.first_name, self.last_name))

    def reversed_name(self, obj):
        return ("%s %s" % (self.last_name, self.first_name))

    def __unicode__(self):
        return ("%s %s" % (self.first_name, self.last_name))

class Publisher(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return ("%s" % (title,))


class Piece(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    publisher = models.ForeignKey(Publisher)
    composer = models.ForeignKey(Composer)
    

class Conductor(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null = True, blank = True)
    last_name = models.CharField(max_length=200)
    prefix = models.CharField(max_length=20, null = True, blank = True)
    suffix = models.CharField(max_length=20, null = True, blank = True)

    def name(self):
        return ("%s %s" % (self.first_name, self.last_name))

    def reversed_name(self, obj):
        return ("%s %s" % (self.last_name, self.first_name))

    def __unicode__(self):
        return ("%s %s" % (self.first_name, self.last_name))

        

class Performance(models.Model):
    piece = models.ForeignKey(Piece)
    conductor = models.ForeignKey(Conductor)
    date = models.DateTimeField('date performed')
    notes = models.TextField(blank = True, null = True)


