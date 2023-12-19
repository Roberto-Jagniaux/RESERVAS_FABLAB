from django.db import models
from datetime import datetime
from django.forms.widgets import SelectDateWidget
from django.utils import timezone
from django.contrib import admin
from django import forms
from django.forms.widgets import DateInput
from django.db import transaction

class stock(models.Model):
    idE = models.AutoField(primary_key=True)
    nomE = models.CharField(max_length=50)

    def __str__(self):
        return f"IDSTOCK {self.idE} - {self.nomE}"



class Bloque(models.Model):
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
    idE = models.ManyToManyField(stock)
    idB = models.ForeignKey(Bloque, null=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Verificar si ya tiene un idR asignado
        if not self.idR:
            self.idR = None  # None para que Django lo genere automáticamente
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nomA}-{self.idB}"



class BloqueAdminForm(forms.ModelForm):
    copiar_bloque = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
        help_text="Seleccione las fechas para copiar el bloque"
    )

    otra_fecha_1 = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
        help_text="Seleccionar nueva fecha",
        label='Nueva fecha',
    )

    otra_fecha_2 = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
        help_text="Seleccionar nueva fecha",
        label='Nueva fecha',
    )

    otra_fecha_3 = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
        help_text="Seleccionar nueva fecha",
        label='Nueva fecha',
    )

    class Meta:
        model = Bloque
        fields = '__all__'

class BloqueAdmin(admin.ModelAdmin):
    form = BloqueAdminForm
    list_display = ('id', 'estados', 'hora_inicio', 'hora_fin', 'fecha')

    def save_model(self, request, obj, form, change):
        copiar_bloque = form.cleaned_data.get('Copiar_bloque')
        otra_fecha_1 = form.cleaned_data.get('Nueva_fecha')
        otra_fecha_2 = form.cleaned_data.get('Nueva_fecha')
        otra_fecha_3 = form.cleaned_data.get('Nueva_fecha')

        if copiar_bloque:
            # Procesa las fechas copiadas
            try:
                with transaction.atomic():
                    fechas = copiar_bloque if isinstance(copiar_bloque, list) else [copiar_bloque]
                    for fecha in fechas:
                        nuevo_Bloque = Bloque(
                            estados=obj.estados,
                            hora_inicio=obj.hora_inicio,
                            hora_fin=obj.hora_fin,
                            fecha=fecha,
                            # Copia otros campos según sea necesario
                        )
                        nuevo_Bloque.save()
            except Exception as e:
                self.message_user(request, f"Error al copiar bloque: {str(e)}", level='error')

        # Procesa las otras fechas
        for fecha in [otra_fecha_1, otra_fecha_2, otra_fecha_3]:
            if fecha:
                try:
                    nuevo_Bloque = Bloque(
                        estados=obj.estados,
                        hora_inicio=obj.hora_inicio,
                        hora_fin=obj.hora_fin,
                        fecha=fecha,
                        # Copia otros campos según sea necesario
                    )
                    nuevo_Bloque.save()
                except Exception as e:
                    self.message_user(request, f"Error al agregar otra fecha: {str(e)}", level='error')

        # Si no hay copiar_bloque ni otras_fechas, utiliza la fecha original
        if not copiar_bloque and not any([otra_fecha_1, otra_fecha_2, otra_fecha_3]):
            obj.save()