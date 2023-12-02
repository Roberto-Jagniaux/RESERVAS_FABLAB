
from django.shortcuts import render
from .models import bloque,stock,reserva
from datetime import datetime,timedelta
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods


import json

@login_required
def bloques(request):
    bloques = bloque.objects.all()
    today = datetime.now().date()
    elementos_stock = stock.objects.all()


    return render(request, 'core/horario2.html', {'bloques': bloques,'today':today,'elementos_stock':elementos_stock})


@login_required
def horario2(request):
    return render(request,"core/horario2.html")

'''def fechas_semana(request):
    # Obtén la fecha actual
    today = datetime.now().date()

    # Calcula la fecha de inicio de la semana (lunes)
    start_of_week = today - timedelta(days=today.weekday())

    # Calcula la fecha de fin de la semana (domingo)
    end_of_week = start_of_week + timedelta(days=6)

    # Pasa las fechas a la plantilla
    context = {
        'start_of_week': start_of_week,
        'end_of_week': end_of_week,
    }

    return render(request, 'core/horario2.html', context)'''


# def datos_reservas(request):
#     if request.method == 'POST':
#         form = reservaForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.succes(request, "Reserva ingresada correctamente")
#             return('horario2')
#     else:
#         form = reservaForm()
#     return render(request, 'horario2/datos_reservas.html')





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







# def datos_reservas(request):
#     if request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         nombre = data.GET.get('nombre', 'Nombre')
#         correo = data.GET.get('correo', 'correo')
#         id_bloque = int(data.GET.get('id_bloque', 'idB'))
#         equipos_seleccionados = data.getlist('equipos_seleccionados', [])
#         # Crear una nueva reserva y guárdala en la base de datos
#         nuevo_bloque = bloque.objects.get(id=id_bloque)
#         nueva_reserva = reserva(nomA=nombre, correo=correo, idB=nuevo_bloque)
#         nueva_reserva.save()
#         # Descontar los equipos seleccionados del stock
#         for id_equipo in equipos_seleccionados:
#             equipo = stock.objects.get(idE=id_equipo)
#             equipo.cantE -= 1
#             equipo.save()
#             # Puedes agregar más lógica aquí según tus necesidades, como verificar si el stock es suficiente, etc.
#         return JsonResponse({'mensaje': 'Reserva creada correctamente'})
#     else:
#         return JsonResponse({'mensaje': 'Método no permitido'})

# def modal_reservas(request):
#     if request.method == 'POST':
#         id_reserva = request.POST.get('idR')
#         id_producto = request.POST.get('idE')
#         nombre = request.POST.get('nombre')
#         correo = request.POST.get('correo')
#         reserva.objects.creada(nombre=nombre,correo=correo)
#         return JsonResponse({'message':'Reserva confirmada correctamente'})
#     else:
#         return JsonResponse({'message':'Error verifique los datos ingresados.'}, status=405)




# def vistaH(request):
#     ins_bloque = bloque.objects.get(id=1)
#     return render(request, 'horario2.html',{'ins_bloque':ins_bloque})