# calculadora

Esta aplicação mostra como se implementa uma página que recolhe informação num formulário, faz seu processamento no back-end, e retorna um resultado associado.

Passos: 
1. Define-se em [forms.py](https://github.com/CR-21-22/calculadora/blob/main/calculadora/forms.py) uma classe para o formulario para recolher o input, neste caso uma expressão matemática numa string.
2. No ficheiro [views.py](https://github.com/CR-21-22/calculadora/blob/main/calculadora/views.py) define-se uma view que cria um objeto `form` vazio da classe formulario.
3. envia-se `form` no contexto, para renderizar o [template](https://github.com/CR-21-22/calculadora/blob/main/calculadora/templates/calculadora/index.html) com o campo do formulário respectivo.
4. quando um formulário é submetido, em [views.py](https://github.com/CR-21-22/calculadora/blob/main/calculadora/views.py) é validado, seus dados extraídos, processados, e neste caso inseridos no contexto, para [apresentar](https://github.com/CR-21-22/calculadora/blob/7934c7f319554484327adf3037fe4c58fe95ac6a/calculadora/templates/calculadora/index.html#L16) no template o resultado.

<img src="https://github.com/CR-21-22/calculadora/blob/main/calculadoraView.png" width="400">
