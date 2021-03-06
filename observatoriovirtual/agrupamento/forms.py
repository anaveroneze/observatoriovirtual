from django import forms
from .models import FoFAlgorithm
from django.core.exceptions import ValidationError
from django.shortcuts import render

# maximum size 25MB input file
def file_size(value):
    limit = 26214400
    if value.size > limit:
        raise ValidationError(('Arquivo muito grande.'
                              'Tamanho máximo deve ser de 20MB.'))
        return render(request, "fof.html")


class FoFForm(forms.Form):
    # Algorithm = forms.ChoiceField(
    #    label="Algorithm", required=True, queryset=FoFAlgorithm.objects.all(),
    #    choices=(("sequentialn2", "FoF O(n²) Sequencial"), ("paralleln2omp", "FoF O(n²) Paralelo OpenMP"), ("paralleln2acc", "FoF O(n²) Paralelo OpenACC")))
    Algorithm = forms.ModelChoiceField(label="Algoritmo", required=True, queryset=FoFAlgorithm.objects.all(), empty_label= "---", initial=3)
    Input = forms.FileField(label="Arquivo de entrada", required=True, validators=[file_size])
    Rperc = forms.FloatField(label="Raio de Percolação", required=True)
    #Numproc = forms.IntegerField(label="Number of processes", required=False)
