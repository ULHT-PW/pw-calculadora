from django.shortcuts import render

# Create your views here.
from calculadora.forms import CalculadoraForm


def index(request):

    resultado = expressao = None

    if request.POST:
        form = CalculadoraForm(request.POST)
        if form.is_valid():
            expressao = form.cleaned_data['expressao']
            try:
                resultado = eval(expressao)
            except:
                resultado = "expressão inválida"

    form = CalculadoraForm(None)

    context = {
        'form': form,
        'resultado': resultado,
        'expressao': expressao
    }

    return render(request, 'calculadora/index.html', context)