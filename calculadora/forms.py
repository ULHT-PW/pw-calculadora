from django import forms

class CalculadoraForm(forms.Form):
    expressao = forms.CharField()