## Como executar

A projeto foi feito usando `python3`. E para executar comando deve ser de acordo com os exemplos a seguir.

### Simulador

O simulador deve receber a entrada no seguinte formato:

```{shell}
$ python3 main.py -s arquivo.txt palavra
```

exemplo de aplicação:

```{shell}
$ python3 main.py -s automatos/entrada.txt 101
```

### Transformação

A Operação de Transformação deve receber a entrada no seguinte formato:

```{shell}
$ python3 main.py -c arquivo.txt
```
Antes de realizar a conversão, é verificado se o autormato passado é uma AFN, caso sim é realizado a conversão, caso não é retornado uma mensagem informando que o mesmo ja é uma AFD.

exemplo de aplicação:

```{shell}
$ python3 main.py -c automatos/entrada.txt
```

### Verificação

A verificação deve receber a entrada no seguinte formato:

```{shell}
$ python3 main.py -v arquivo.txt palavras.txt
```
Antes de ser realizada a verificação é feita a verificação se o automato está inserido de forma correta no arquivo de texto. Se sim, é feita a analise para ver se as palavras lidas no arquivo pertencem a gramatica do afd equivalente

exemplo de aplicação:

```{shell}
$ python3 main.py -l automatos/entrada.txt automatos/palavras.txt
```

### Formato do arquivo de entrada

O o arquivo de entrada contendo a descrição do autômato deverá obedecer ao seguinte formato:

```{text}
estados <lista com os nomes dos estados>
inicial <nome do estado inicial>
aceita <lista com os nomes dos estados finais>
<transições>
````

Note que estados, inicial e aceita são palavras reservadas.

`<transições>` descreve cada transição do autômato (é uma lista) e tem o formato:

```{text}
estado1 simbolo(alfabeto) estado2
````

siginifcando que a transição leva do estado1 para o estado2 lendo o símbolo do alfabeto.
Um exemplo de arquivo de entrada seria:

```{text}
estados A B C
inicial A
aceita B
A 0 B
B 0 A
A 1 A
B 1 B
A 1 C
```

Todos os autômatos que serão testados terão esse formato. Use o símbolo h para denotar o símbolo vazio.
