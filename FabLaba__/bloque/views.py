
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


    return render(request, 'core/horario2.html', {'bloques': bloques,'today':today,'elementos_stock':elementos_stock})

@login_required
def horario2(request):
    return render(request,"core/horario2.html")


"""@csrf_exempt
def datos_reservas(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            correo = request.POST.get('correo')
            id_bloque = request.POST.get('id_bloque', '')

            # Verificar si id_bloque es un valor válido antes de hacer la consulta
            if not id_bloque.isdigit():
                raise ValueError("El valor de 'id_bloque' no es un número válido.")

            # Obtener el bloque asociado a la reserva
            bloque_reservado = Bloque.objects.get(id=int(id_bloque))

            # Resto de tu lógica aquí...
            
        except Bloque.DoesNotExist:
            return JsonResponse({'message': 'El bloque no existe.'}, status=400)
        except ValueError as ve:
            return JsonResponse({'message': f'Error: {str(ve)}'}, status=400)
        except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=500)

    else:
        return JsonResponse({'message': 'Método no permitido.'}, status=405)
"""
"""test 2
def datos_reservas(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        id_bloque = request.POST.get('id_bloque', '')

        try:
            # Obtener el bloque asociado a la reserva
            bloque = Bloque.objects.get(id=id_bloque)

            # Verificar si el bloque está disponible antes de hacer la reserva
            if Bloque.estados == 'Disponible':
                # Actualizar el estado del bloque a "Reservado"
                Bloque.estados = 'Reservado'
                Bloque.save()

                # Crear una nueva reserva con el bloque asociado
                nueva_reserva = Reserva(nomA=nombre, correo=correo, idB=bloque)
                nueva_reserva.save()

                return JsonResponse({'message': 'Reserva hecha exitosamente.'})
            else:
                return JsonResponse({'message': 'El bloque no está disponible para reserva.'}, status=400)

        except Bloque.DoesNotExist:
            return JsonResponse({'message': 'El bloque no existe.'}, status=400)

    else:
        return JsonResponse({'message': 'Método no permitido.'}, status=405)"""


"""
working
def datos_reservas(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        equipos_seleccionados = request.POST.getlist('equipos_seleccionados', [])

        # Crear una nueva reserva
        nueva_reserva = reserva(nomA=nombre, correo=correo)
        nueva_reserva.save()  # Guardar la reserva antes de asignar la relación many-to-many

        # Asignar equipos seleccionados a la reserva
        nueva_reserva.idE.set(equipos_seleccionados)

        return JsonResponse({'message': 'Reserva Hecha Exitosamente.'})
    else:
        return JsonResponse({'message': 'Método no permitido.'}, status=405)

from django.http import JsonResponse
import json"""

def datos_reservas(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        equipos_seleccionados = request.POST.getlist('equipos_seleccionados', [])

        # Crear una nueva reserva
        nueva_reserva = reserva(nomA=nombre, correo=correo)
        nueva_reserva.save()  # Guardar la reserva antes de asignar la relación many-to-many

        # Asignar equipos seleccionados a la reserva
        nueva_reserva.idE.set(equipos_seleccionados)

        return JsonResponse({'message': 'Reserva Hecha Exitosamente.'})
    else:
        return JsonResponse({'message': 'Método no permitido.'}, status=405)




"""def datos_reservas(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        print(request.body)  # Imprimir el cuerpo de la solicitud para depuración
        data = json.loads(request.body)
        nombre = data.get('nombre', '')
        correo = data.get('correo', '')
        id_bloque = data.get('id_bloque', '')
        equipos_seleccionados = data.getlist('equipos_seleccionados', [])

        # Crear una nueva reserva y guárdala en la base de datos
        nuevo_bloque = Bloque.objects.get(id=id_bloque)
        nueva_reserva = Reserva(nomA=nombre, correo=correo, idB=nuevo_bloque)
        nueva_reserva.save()

        # Descontar los equipos seleccionados del stock
        for id_equipo in equipos_seleccionados:
            equipo = stock.objects.get(idE=id_equipo)
            equipo.cantE -= 1
            equipo.save()
            # Puedes agregar más lógica aquí según tus necesidades, como verificar si el stock es suficiente, etc.

        return JsonResponse({'mensaje': 'Reserva creada correctamente'})
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)"""


"""
cone ste funciona el cambio de boton a confirmado
def confirmar_reserva(request):
    if request.method == 'POST':
        bloque_id = request.POST.get('bloque_id')
        # Obtén el objeto Bloque
        bloque = get_object_or_404(Bloque, id=bloque_id)
        
        # Actualiza el estado del bloque a 'Confirmado'
        bloque.estados = 'Reservado'
        bloque.save()

        # Puedes realizar otras acciones aquí según tus necesidades

        return JsonResponse({'message': 'Reserva confirmada satisfactoriamente.'})
    else:
        return JsonResponse({'error': 'Método no permitido.'})"""


from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Bloque, reserva

def confirmar_reserva(request):
    if request.method == 'POST':
        bloque_id = request.POST.get('bloque_id')
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        equipos_seleccionados = request.POST.getlist('equipos_seleccionados')

        # Obtener el bloque correspondiente
        bloque = get_object_or_404(Bloque, id=bloque_id)

        # Crear la reserva y asociarla al bloque
        reserva_obj = reserva.objects.create(nomA=nombre, correo=correo, idB=bloque)

        # Asociar los equipos seleccionados al bloque
        bloque.idE.set(equipos_seleccionados)

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