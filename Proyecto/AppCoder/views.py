from django.shortcuts import render
from django.http import HttpResponse

from AppCoder.models import Curso
from django.core import serializers 

from AppCoder.forms import CursoFormulario 


def buscar(request):
    comision_views = request.GET ['comision']
    cursos_todos = Curso.objects.filter(comision=comision_views) 
    return render (request,"AppCoder/resultadoCurso.html",{"comision":comision_views,"cursos":cursos_todos})

def buscarcurso(request):
    return render(request,'AppCoder/busquedaCurso.html')

def inicio(request):
    return render(request,'AppCoder/inicio.html')

def cursos(request):
    if request.method == "POST":
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso=Curso(nombre=informacion["nombre"], comision=informacion["comision"], numero_dia=informacion["numero_dia"])
                  curso.save()
                  return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()
 
    return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})

def profesores(request):
    return HttpResponse('Vistas de Profesores')

def cursosapi(request):
    cursos_todos=Curso.objects.all()
    return HttpResponse(serializers.serialize('json',cursos_todos))
    
    

