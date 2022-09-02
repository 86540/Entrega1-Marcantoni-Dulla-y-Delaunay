from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.forms import CursoFormulario, EstudiantesFormulario, ProfesoresFormulario



def curso(request):

      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)


def curso(request):
      return render(request, "AppCoder/curso.html")

def Estudiantes(request):
      return render(request, "AppCoder/Estudiantes.html")

def Profesores(request):
      return render(request, "AppCoder/Profesores.html")

def inicio(request):
      return render(request, "AppCoder/inicio.html")


def cursoFormulario(request):
      if request.method=='POST':
            miformulario=CursoFormulario(request.POST)
            if miformulario.is_valid():
                  info=miformulario.cleaned_data
                  nombre=info.get("nombre")
                  comision=info.get("comision")
                  curso=Curso(nombre=nombre, comision=comision)
                  curso.save()
                  return render(request,"AppCoder/inicio.html", {"mensaje":"curso creado"})
            else:
                  return render (request, "AppCoder/cursoFormulario" ,{"mensaje":"error"})
      else:
            miformulario=CursoFormulario()
            return render(request, "Appcoder/cursoFormulario.html" , {"formulario":miformulario})
      
def estudiantesFormulario(request):
      if request.method=='POST':
            miformulario= EstudiantesFormulario(request.POST)
            if miformulario.is_valid():
                  info=miformulario.cleaned_data
                  nombre=info.get("nombre")
                  nota=info.get("nota")
                  email=info.get("email")
                  estudiante=Estudiantes(nombre=nombre, nota=nota, email=email)
                  estudiante.save()
                  return render(request,"AppCoder/inicio.html", {"mensaje":"estudiante creado"})
            else:
                  return render (request, "AppCoder/estudiantesFormulario" ,{"mensaje":"error"})
      else:
            miformulario=EstudiantesFormulario()
            return render(request, "Appcoder/estudiantesFormulario.html" , {"formulario":miformulario})
      
      
      
      
      
def profesoresFormulario(request):
      if request.method=='POST':
            miformulario= ProfesoresFormulario(request.POST)
            if miformulario.is_valid():
                  info=miformulario.cleaned_data
                  nombre=info.get("nombre")
                  apellido=info.get("nota")
                  profesion=info.get("email")
                  profesores=Profesores(nombre=nombre, apellido=apellido, profesion=profesion)
                  profesores.save()
                  return render(request,"AppCoder/inicio.html", {"mensaje":"profe creado"})
            else:
                  return render (request, "AppCoder/profesoresFormulario" ,{"mensaje":"error"})
      else:
            miformulario=ProfesoresFormulario()
            return render(request, "Appcoder/profesoresFormulario.html" , {"formulario":miformulario})
      
      
def busquedaCamada(request):
      return render(request, 'AppCoder/busquedaCamada.html')

def buscar(request):
      if request.GET['camada']:
            camada= request.GET['camada']
            cursos=Curso.objects.filter(camada__icontains=camada)
      
            return render (request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos, "camada":camada})
      else:
            respuesta= "no enviaste datos"
            
      return HttpResponse(respuesta)
                     

      
      

      
      respuesta= f"Estoy buscando la camada nro:{request.GET['camada']}"
      return HttpResponse(respuesta)