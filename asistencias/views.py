from django.shortcuts import render
from .models import Asistencia

# Create your views here.
def crear(request):
    if request.method == "POST":
        asistencias = Asistencia(
            tipo_de_documento = request.POST["tipo_de_documento"],
            documento = request.POST["documento"],
            nombre = request.POST["nombre"],
            apellidos = request.POST["apellidos"],
            whatsapp = request.POST["whatsapp"],
            fecha = request.POST["fecha"],
            asistio = request.POST["asistio"]
        )

        asistencias.save() 
    return render(request, "asistencias/formulario.html")


def listar(request):
    
    asistencias = Asistencia.objects.all()
    return render(
        request,
        "asistencias/lista.html",
        {"asistencias": asistencias}
    )


def detalle(request,id):
    asistencias = Asistencia.objects.get(id=id)#SELECT * FROM Asistencia WHERE id=7
    return render(
        request, 
        "asistencias/detalle.html",
        {"asistencias": asistencias})


def editar(request, id):

    asistencias = Asistencia.objects.get(id=id)#SELECT * FROM Asistencia WHERE id=7
    
    if request.method=="POST":
        asistencias.tipo_de_documento = request.POST["tipo_de_documento"] 
        asistencias.documento = request.POST["documento"] 
        asistencias.nombre = request.POST["nombre"] 
        asistencias.apellidos = request.POST["apellidos"]
        asistencias.whatsapp = request.POST["whatsapp"]
        asistencias.fecha = request.POST["fecha"]
        asistencias.asistio = request.POST["asistio"] == "True"


        asistencias.save() 

        return render(
            request,
            "asistencias/detalle.html",
            {"asistencias": asistencias}
        )
        
    
    return render(
        request,
        "asistencias/formulario.html",
        {"asistencias": asistencias}
    )

def eliminar(request,id):
    asistencias = Asistencia.objects.get(id=id)
    asistencias.delete()
    return render(
            request,
            "asistencias/detalle.html",
            {"asistencias": asistencias}
        )
