# calculadora

Esta aplicação mostra como se implementa uma página que recolhe informação num formulário, faz seu processamento no back-end, e retorna um resultado associado.

Passos: 
1. Define-se em [forms.py](https://github.com/CR-21-22/calculadora/blob/main/calculadora/forms.py) uma classe para o formulario, que servirá para recolher a(s) info(s) inserida(s) no formulário. Neste caso existe apenas um input, uma expressão matemática guardada como uma string. 
2. No ficheiro [views.py](https://github.com/CR-21-22/calculadora/blob/main/calculadora/views.py) na respetiva view (index no exemplo), cria-se um objeto `form` vazio da classe formulario.
3. envia-se o `form` no contexto, para renderizar o [template](https://github.com/CR-21-22/calculadora/blob/main/calculadora/templates/calculadora/index.html), sendo inseridos, no formulário, os respetivos campos para recolher informação desejada.
4. quando um formulário é submetido com dados, em [views.py](https://github.com/CR-21-22/calculadora/blob/main/calculadora/views.py) os dados são validados, seus dados extraídos, processados, e neste caso inseridos de volta no contexto, para [apresentar](https://github.com/CR-21-22/calculadora/blob/7934c7f319554484327adf3037fe4c58fe95ac6a/calculadora/templates/calculadora/index.html#L16) no template o resultado.

![praia](https://user-images.githubusercontent.com/42048382/143572481-5e63222c-6653-4d0b-92b8-4d027f284648.png)


https://user-images.githubusercontent.com/42048382/143500089-452e00d1-d95a-47e4-baac-cf1851796bf1.mp4

