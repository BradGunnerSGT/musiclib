from libraries.models import Publisher
from libraries.models import Composer
from libraries.models import Title
from libraries.models import Conductor
from libraries.models import Soloist
from libraries.models import Performance
from django.contrib import admin



admin.site.register(Publisher)
admin.site.register(Composer)
admin.site.register(Piece)
admin.site.register(Conductor)
admin.site.register(Soloist)
admin.site.register(Performance)
