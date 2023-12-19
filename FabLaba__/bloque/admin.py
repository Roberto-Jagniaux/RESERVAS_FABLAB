from django.contrib import admin
from .models import Bloque
from .models import reserva
from .models import stock
from .models import BloqueAdmin



admin.site.register(Bloque, BloqueAdmin)
admin.site.register(reserva)
admin.site.register(stock)
