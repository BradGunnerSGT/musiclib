from django.db import models

# Create your models here.
class MyPerson(models.Model):
    prefix = models.CharField(max_length=20, null = True, blank = True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null = True, blank = True)
    last_name = models.CharField(max_length=200)
    suffix = models.CharField(max_length=20, null = True, blank = True)

    def name(self):
        return ("%s %s %s" % (self.first_name, self.middle_name, self.last_name))

    def full_name(self):
        return ("%s %s %s" % (self.first_name, self.middle_name, self.last_name))

    def reversed_name(self):
        return ("%s %s" % (self.last_name, self.first_name))

    def __unicode__(self):
        return ("%s %s" % (self.first_name, self.last_name))

class Composer(MyPerson):   
    def __unicode__(self):
        return ("%s %s %s" % (self.first_name, self.middle_name, self.last_name))

class Conductor(MyPerson):
    pass

class Soloist(MyPerson):
    pass

class Publisher(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return ("%s" % (self.title,))


class Title(models.Model):
    name = models.CharField(max_length=200)
    publisher = models.ForeignKey(Publisher)
    composer = models.ForeignKey(Composer)
    def __unicode__(self):
        return ("%s" % (self.name,))
    

class Performance(models.Model):
    piece = models.ForeignKey(Piece)
    conductor = models.ForeignKey(Conductor)
    date = models.DateTimeField('date performed')
    notes = models.TextField(blank = True, null = True)

#    def __unicode__(self):
#        return ("%s" % (self.piece.title, self.date))
