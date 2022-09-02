from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader


def saludo (request):
    return HttpResponse("hola mundo!")
    
def probandohtml (request, edad):
    annio_nacimiento=2022-int(edad)
    plantilla=loader.get_template('template1.html')
     #aca van los datos que voy a mostrar desde la base de datos 
    diccionario={'probandohtml':annio_nacimiento}
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)



