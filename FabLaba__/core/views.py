from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

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
    return render(request, "core/reportes.html")

def Admin_view(request):
    return render(request, "core/admin_view.html")




