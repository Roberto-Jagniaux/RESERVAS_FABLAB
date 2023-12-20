
from django.db import models
from accounts.models import Project
from django.shortcuts import render
from .models import Bloque,stock,reserva
from datetime import datetime,timedelta
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json

@login_required
def bloques(request):
    bloques = Bloque.objects.all()
    today = datetime.now().date()
    elementos_stock = stock.objects.all()
    user = request.user


    return render(request, 'core/horario2.html', {'bloques': bloques,'today':today,'elementos_stock':elementos_stock})

@login_required
def horario2(request):
    return render(request,"core/horario2.html")


def datos_reservas(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        equipos_seleccionados = request.POST.getlist('equipos_seleccionados', [])
        perfil_usuario = request.user.profile  # Asegúrate de tener el campo 'profile' en tu modelo de usuario
        # Crear una nueva reserva
        nueva_reserva = reserva(nomA=nombre, correo=correo)
        nueva_reserva.save()  # Guardar la reserva antes de asignar la relación many-to-many

        # Asignar equipos seleccionados a la reserva
        nueva_reserva.idE.set(equipos_seleccionados)


        return JsonResponse({'message': 'Reserva Hecha Exitosamente.'})
    else:
        return JsonResponse({'message': 'Método no permitido.'}, status=405)







def confirmar_reserva(request):
    if request.method == 'POST':
        bloque_id = request.POST.get('bloque_id')
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        equipos_seleccionados = request.POST.getlist('equipos_seleccionados')

        # Obtener el bloque correspondiente
        bloque = get_object_or_404(Bloque, id=bloque_id)

        # Crear la reserva y asociarla al bloque
        reserva_obj = reserva(nomA=nombre, correo=correo, idB=bloque)

        # Asociar los equipos seleccionados al bloque
        bloque.idE.set(equipos_seleccionados)

        # Obtener el perfil del usuario actual
        perfil_usuario = request.user.profile

        # Asociar el proyecto del usuario a la reserva
        reserva_obj.proyecto_usuario = perfil_usuario.project
        reserva_obj.save()

        # Actualizar el estado del bloque a 'Reservado'
        bloque.estados = 'Reservado'
        bloque.save()

        return JsonResponse({'message': 'Reserva confirmada correctamente.'})
    else:
        return JsonResponse({'message': 'Error en la solicitud.'}, status=400)



def obtener_stock_disponible(request, bloque_id):
    try:
        bloque = Bloque.objects.get(id=bloque_id)
        stock_disponible = bloque.idE.all().exclude(reserva__idB=bloque)
        stock_info = [{'id': stock.idE, 'nombre': stock.nomE} for stock in stock_disponible]
        return JsonResponse({'stock_disponible': stock_info})
    except Bloque.DoesNotExist:
        return JsonResponse({'error': 'Bloque no encontrado'}, status=404)