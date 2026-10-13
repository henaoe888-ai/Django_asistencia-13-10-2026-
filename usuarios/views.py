from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def iniciar_sesion(request):

    if request.method == "POST":

        usuario = authenticate(request,
        username = request.POST["username"],
        password = request.POST["password"]
        )

        if usuario is not None:
            login(request, usuario)
            destino = request.GET.get("next", "/asistencias/listar/")
            return redirect(destino)

        return render(
            request,
            "usuarios/login.html",
            {"error": "Usuario o contraseña incorrectos"}
        )

    #Redirecciona si el método no es POST
    return render(
        request,
        "usuarios/login.html",
    )

#Cierra sesión
def cerrar_sesion(request):
    logout(request)
    return redirect("/usuarios/login/")

        