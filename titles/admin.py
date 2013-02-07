from titles.models import Publisher
from titles.models import Arranger
from titles.models import Composer
from titles.models import OrchestraType
from titles.models import ScoreType
from titles.models import ConcertType
from titles.models import SoloInstrument
from titles.models import Title
from titles.models import TitleNote
from titles.models import Conductor
from titles.models import Soloist
from titles.models import ConcertMaster
from titles.models import Location
from titles.models import Performance
from titles.models import PerformanceNote
from django.contrib import admin

# Utility classes
class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ("created","modified",)

class TitleAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'composer', 'publisher')

class NameAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name')

class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'concert_type')

    
admin.site.register(Publisher)
admin.site.register(Arranger, NameAdmin)
admin.site.register(Composer, NameAdmin)
admin.site.register(OrchestraType)
admin.site.register(ScoreType)
admin.site.register(ConcertType)
admin.site.register(SoloInstrument)
admin.site.register(Title, TitleAdmin)
admin.site.register(TitleNote, NoteAdmin)
admin.site.register(Conductor, NameAdmin)
admin.site.register(Soloist, NameAdmin)
admin.site.register(ConcertMaster, NameAdmin)
admin.site.register(Location)
admin.site.register(Performance, PerformanceAdmin)
admin.site.register(PerformanceNote, NoteAdmin)
