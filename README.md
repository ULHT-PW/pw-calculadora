# calculadora

Esta aplicação mostra como se implementa uma página que recolhe informação num formulário, faz seu processamento no back-end, e retorna um resultado associado.

Passos: 
1. Define-se em [forms.py](https://github.com/ULHT-PW/calculadora/blob/main/calculadora/forms.py) uma classe para o formulario, que servirá para recolher a(s) info(s) inserida(s) no formulário. Neste caso existe apenas um input, uma expressão matemática guardada como uma string. 
2. No ficheiro [views.py](https://github.com/ULHT-PW/calculadora/blob/main/calculadora/views.py) na respetiva view (index no exemplo), cria-se um objeto `form` vazio da classe formulario.
3. envia-se o `form` no contexto, para renderizar o [template](https://github.com/ULHT-PW/calculadora/blob/main/calculadora/templates/calculadora/index.html), sendo inseridos, no formulário, os respetivos campos para recolher informação desejada.
4. quando o utilizador insere uma expressão matemática no formulário e o submete, a mesma view `index` é chamada, sendo agora a condição `if request.POST:` válida, em [views.py](https://github.com/ULHT-PW/calculadora/blob/main/calculadora/views.py) os dados são validados, seus dados extraídos, processados, e neste caso inseridos de volta no contexto, para [apresentar](https://github.com/ULHT-PW/calculadora/blob/7934c7f319554484327adf3037fe4c58fe95ac6a/calculadora/templates/calculadora/index.html#L16) no template o resultado.

https://user-images.githubusercontent.com/42048382/143500089-452e00d1-d95a-47e4-baac-cf1851796bf1.mp4

