from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from bloque.models import reserva
from django.db.models import Q
from datetime import datetime

def exit(request):
    logout(request)
    return redirect('inicio')  # Redirige a la página de inicio


def inicio(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            user_groups = user.groups.all()
            for group in user_groups:
                if group.name == "Administrador":
                    return redirect('/admin_view')  # Redirige a la página de admin
            # Si el usuario no es Administrador, redirige a la página '/horario2'
            return redirect('/horario2')

        else:
            messages.error(request, 'Credenciales inválidas. Inténtelo de nuevo.')

    # Devuelve una respuesta HttpResponse aunque las credenciales sean inválidas
    return render(request, "registration/login.html")

def reportes(request):
    # Obtener los parámetros de fecha desde la URL
    fecha_desde_str = request.GET.get('fecha_desde')
    fecha_hasta_str = request.GET.get('fecha_hasta')

    # Convertir las cadenas de fecha a objetos datetime
    fecha_desde = datetime.strptime(fecha_desde_str, "%Y-%m-%d") if fecha_desde_str else None
    fecha_hasta = datetime.strptime(fecha_hasta_str, "%Y-%m-%d") if fecha_hasta_str else None

    # Filtrar las reservas según las fechas
    if fecha_desde and fecha_hasta:
        reservas = reserva.objects.filter(idB__fecha__range=[fecha_desde, fecha_hasta])
    else:
        reservas = reserva.objects.all().order_by('idB__fecha', 'idB__hora_inicio')

    # Obtener el stock reservado en cada bloque
    stock_reservado_por_bloque = {}
    for reserva_item in reservas:
        bloque_reservado = reserva_item.idB
        stock_reservado = bloque_reservado.idE.all() if bloque_reservado else []
        stock_reservado_por_bloque[reserva_item.idR] = stock_reservado

    return render(request, 'core/reportes.html', {'reservas': reservas, 'stock_reservado_por_bloque': stock_reservado_por_bloque})

def Admin_view(request):
    return render(request, "core/admin_view.html")




