from django.contrib import admin
from .models import bloque
from .models import reserva
from .models import stock



admin.site.register(bloque)
admin.site.register(reserva)
admin.site.register(stock)
