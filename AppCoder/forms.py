from django import forms
    
class CursoFormulario(forms.Form):
    nombre= forms.CharField(max_length=50)
    comision = forms.IntegerField()
    
class EstudiantesFormulario(forms.Form):
    nombre= forms.CharField(max_length=50)
    comision = forms.IntegerField()
    
class ProfesoresFormulario(forms.Form):
    nombre= forms.CharField(max_length=50)
    comision = forms.IntegerField()