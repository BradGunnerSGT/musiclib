from django.db import models

# Create your models here.
class BaseModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)



class NamedModel(BaseModel):
    class Meta:
        abstract = True
        ordering = ['name']

    name = models.CharField(max_length=200, unique = True)

    def __unicode__(self):
        return ("%s" % (self.name,))
    


class NoteModel(BaseModel):
    class Meta:
        abstract = True

    note = models.CharField(max_length=200)

    def __unicode__(self):
        snip = 20
        elip = ""
        if (len(self.note) > snip):
            elip = "..."
        return ("%s%s" % (self.note[:snip], elip))



class PersonModel(BaseModel):
    class Meta:
        abstract = True
        ordering = ['last_name', 'first_name', 'middle_name', 'suffix']

    prefix = models.CharField("title", max_length=20, null = True, blank = True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null = True, blank = True)
    last_name = models.CharField(max_length=200)
    suffix = models.CharField(max_length=20, null = True, blank = True)

    def __unicode__(self):
        return ("%s %s %s %s %0s" % (self.prefix, self.first_name, self.middle_name,
		self.last_name, self.suffix)).strip().replace('  ', ' ')



class Composer(PersonModel):   
    pass



class Conductor(PersonModel):
    pass



class Soloist(PersonModel):
    pass



class Editor(PersonModel):
    pass



class Arranger(PersonModel):
    pass



class ConcertMaster(PersonModel):
    pass



class Publisher(NamedModel):
    pass



class Distributor(NamedModel):
    pass



class OrchestraType(NamedModel):
    pass



class ScoreType(NamedModel):
    pass



class ConcertType(NamedModel):
    pass



class SoloInstrument(NamedModel):
    pass



class Location(NamedModel):
    pass



class Title(BaseModel):
    class Meta:
        ordering = ['number']
    number = models.PositiveIntegerField(unique = True)
    title = models.CharField(max_length=200)
    composer = models.ForeignKey(Composer)
    publisher = models.ForeignKey(Publisher)
    distributor = models.ForeignKey(Distributor, null = True, blank = True)
    arranger = models.ForeignKey(Arranger, null = True, blank = True)
    editor = models.ForeignKey(Editor, null = True, blank = True)
    instrumentation = models.CharField(max_length=200)
    score_type = models.ForeignKey(ScoreType, null = True, blank = True)
    orchestra_type = models.ForeignKey(OrchestraType, null = True, blank = True)
    solo_instruments = models.ManyToManyField(SoloInstrument, null = True, blank = True)
    
    def __unicode__(self):
        return ("%s by %s" % (self.title, self.composer))
    


class Performance(BaseModel):
    title = models.ForeignKey(Title)
    date = models.DateField('performance date')
    conductor = models.ForeignKey(Conductor)
    location = models.ForeignKey(Location)
    duration = models.CharField(max_length=10, blank = True, null = True)
    concert_type = models.ForeignKey(ConcertType, help_text = "concert type")
    concert_master = models.ForeignKey(ConcertMaster, help_text = "concert master")
    soloist = models.ManyToManyField(Soloist, null = True, blank = True)
    info = models.CharField("additional info", max_length=200, blank = True, null = True)
    # eventually, we want to be able to upload attachments such as a copy of the score with
    # the bowings for this performance

    def __unicode__(self):
        return ("%s on %s" % (self.title, self.date))



class TitleNote(NoteModel):
    title = models.ForeignKey(Title)



class PerformanceNote(NoteModel):
    performance = models.ForeignKey(Performance)
