# calculadora

Esta aplicação mostra como se implementa uma página que recolhe informação num formulário, faz seu processamento no back-end, e retorna um resultado associado.

Passos: 
1. Define-se em [forms.py](https://github.com/CR-21-22/calculadora/blob/main/calculadora/forms.py) uma classe para o formulario, que servirá para recolher a(s) info(s) inserida(s) no formulário. Neste caso existe apenas um input, uma expressão matemática guardada como uma string. 
2. No ficheiro [views.py](https://github.com/CR-21-22/calculadora/blob/main/calculadora/views.py) na respetiva view (index no exemplo), cria-se um objeto `form` vazio da classe formulario.
3. envia-se o `form` no contexto, para renderizar o [template](https://github.com/CR-21-22/calculadora/blob/main/calculadora/templates/calculadora/index.html), sendo inseridos, no formulário, os respetivos campos para recolher informação desejada.
4. quando um formulário é submetido com dados, em [views.py](https://github.com/CR-21-22/calculadora/blob/main/calculadora/views.py) os dados são validados, seus dados extraídos, processados, e neste caso inseridos de volta no contexto, para [apresentar](https://github.com/CR-21-22/calculadora/blob/7934c7f319554484327adf3037fe4c58fe95ac6a/calculadora/templates/calculadora/index.html#L16) no template o resultado.

<img src="https://github.com/CR-21-22/calculadora/blob/main/calculadoraView.png" width="400">
