from pieces.models import Publisher
from pieces.models import Composer
from pieces.models import Piece
from pieces.models import Conductor
from pieces.models import Performance
from django.contrib import admin



class ConductorAdmin(admin.ModelAdmin):
    # change the way the object is displayed on the admin site listing
    pass

admin.site.register(Publisher)
admin.site.register(Composer)
admin.site.register(Piece)
admin.site.register(Conductor, ConductorAdmin)
admin.site.register(Performance)
