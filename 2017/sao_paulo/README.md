# HACKAFLAG São Paulo 2017
```
                   +++    HACKAFLAG - Mais ou Menos   +++

 [+] A Vagry Corporation é uma empresa que produz processadores, e está
    atrás dos seus serviços para ajudá-los na otimização de uma sequência
    intercalada de operações de adição e subtração, dada uma determinada
    sequência de números. As operações seguem a estrutura de uma árvore, de
    forma a reduzir a lista de números a um único valor, intercalando as suas
    operações, como no exemplo da lista [1, 3, 5, 7, 9]


                           1     3     5     7     9
                              +     -     +     -
                              4    -2    12    -2
                                 +     -     +
                                 2    -14   10
                                    -     +
                                   16    -4
                                       -
                                      20

     A resposta correta é 20.

 [+] Sua tarefa é gerar as repostas para os testes que serão realizados,
    futuramente no processador da Vagry. Será informado para você três inteiros
    (0 <= I, T < 20000; P > 0), que representam, respectivamente, o início da
    lista de valores, o término da lista de valores e o passo (intervalo) entre
    cada um dos valores da lista.

 [+] Como o processador possui arquitetura limitada, você deverá retornar
    o resto da divisão da sua resposta pelo valor 2^31 - 1. Segue um exemplo
    utilizando a operação de resto para os valores de I = 0, T = 10 e P = 3

                              0     3     6     9
                                 +     -     +
                                 3    -3    15
                                    -     +
                                    6    12
                                       -
                                      -6      %       2 ^ 31 - 1

                                           2147483641

    A resposta correta é 2147483641.

 [+] O limite para cada resposta será de 5 segundos.
 
 [+] Para começar, digite start: start
     Iniciando...

 [+] Teste 1 - (I, T, P): 1, 4, 3
     A resposta é: 1
 [+] Correto!
 ```

## Execução
```
$ python2.7 hackaflag.py
```

## Flag
```
HACKAFLAG{b1n0mI0_d3_flAg$}
```

BY : flavianogjc