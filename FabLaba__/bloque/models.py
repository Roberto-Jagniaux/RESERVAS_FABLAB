from django.db import models
from datetime import datetime
from django.forms.widgets import SelectDateWidget

from django.utils import timezone

class stock(models.Model):
    idE = models.AutoField(primary_key=True)
    nomE = models.CharField(max_length=50)

    def __str__(self):
        return f"IDSTOCK {self.idE} - {self.nomE}"



class bloque(models.Model):
    id = models.AutoField(primary_key=True)
    estados = models.CharField(
        max_length=15,
        choices=[
            ('Reservado', 'Reservado'),
            ('Disponible', 'Disponible'),
            ('No Disponible', 'No Disponible'),
        ],
        default='No Disponible'
    )
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    fecha = models.DateField()
    idE = models.ManyToManyField(stock)

    def __str__(self):
        return f"IDB{self.id}- Fecha {self.fecha}"





class reserva(models.Model):
    idR = models.AutoField(primary_key=True)
    nomA = models.CharField(max_length=25)
    correo = models.CharField(max_length=50)
    idB = models.ForeignKey(bloque, null=True, on_delete=models.CASCADE)
    idE = models.ManyToManyField(stock)

    def save(self, *args, **kwargs):
        # Verificar si ya tiene un idR asignado
        if not self.idR:
            self.idR = None  # None para que Django lo genere automáticamente
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nomA}-{self.idB}"



