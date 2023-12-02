from django.contrib import admin
from django.urls import path,include
from core import views as core_views
from bloque import views as bloque_views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', core_views.inicio, name='inicio'),
    path('horario2/', bloque_views.bloques, name='horario2'),
    path('horario2/datos_reservas/', bloque_views.datos_reservas, name='datos_reservas'),
    path('horario2/modal_reservas/', bloque_views.datos_reservas, name='modal_reservas'),
    path('logout/', core_views.exit, name='exit'),
    path('admin/', admin.site.urls),
    path('reportes/', core_views.reportes, name='reportes'),
    path('accounts/', include('django.contrib.auth.urls')),

]
