# HACKAFLAG Rio de Janeiro 2017
```
                   +++    HACKAFLAG - Bugnário    +++

 [+] A Vagry Corporation, empresa do ramo de hardware e software, encontrou
    um bug muito estranho em um de seus processadores. Sempre que esse
    processador recebe um valor na sua entrada, e a representação binária desse
    valor possui dois uns lado a lado, o processador "crasha". Como a empresa
    não gosta de desperdiçar recursos, ela pretende utilizar o processador
    evitando valores que possam gerar problemas em seu uso. Dessa forma, você
    foi contradado para descobrir, em uma lista de valores, quantos deles podem
    ser utilizados.

 [+] Sua tarefa é, dado um valor N, verificar todos os números P (0 <= P < N) 
    e informar a quantidade desses valores que podem ser utilizados pelo
    processador. Segue um exemplo para N = 10.

    0 = 0b0000 - OK
    1 = 0b0001 - OK
    2 = 0b0010 - OK
    3 = 0b0011 - NÃO
    4 = 0b0100 - OK
    5 = 0b0101 - OK
    6 = 0b0110 - NÃO
    7 = 0b0111 - NÃO
    8 = 0b1000 - OK
    9 = 0b1001 - OK

    A resposta correta é 7.

 [+] O limite para cada resposta será de 3 segundos.
 
 [+] Para começar, digite start: start
      Iniciando...

 [+] Teste 1 - (N): 5
     A resposta é: 4
 [+] Correto!
 ```

## Execução
```
$ python2.7 hackaflag.py
```

## Flag
```
HACKAFLAG{c0ntad0r_D3_zEr0s}
```

BY : flavianogjc