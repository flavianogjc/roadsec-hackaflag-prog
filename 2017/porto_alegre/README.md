# HACKAFLAG Porto Alegre 2017
```
                   +++    HACKAFLAG - Cassino II     +++

 [+] Com o sucesso da primeira edição, o Roadsec decidiu expandir os seus
    jogos e lançar uma versão modificada do seu popular jogo de cartas.

 [+] Esse jogo funciona da seguinte maneira: Dada uma sequência de cartas
    numeradas e em uma ordem específica, o jogador deve ir escolhendo cartas
    alternadamente sendo uma carta para pontuar, e em seguida uma carta para ser
    descartadas das pontas das cartas distribuídas. Quando não restarem mais
    cartas na mesa, a pontuação final será a soma das cartas escolhidas pelo
    participante.

 [+] O jogador vence o jogo se a soma das cartas for a maior possível dada
    a disposição inicial das cartas ao jogador.

 [+] Exemplo de uma rodada com 6 cartas: 
    
    Cartas: 5   3   2   9   4   1
                
    Entre 5 e 1, escolhe  5 para pontuar
    Entre 3 e 1, escolhe  1 para descartar
    Entre 3 e 4, escolhe  4 para pontuar
    Entre 3 e 9, escolhe  3 para descartar
    Entre 2 e 9, escolhe  9 para pontuar
    E finalmente escolhe  2 para descartar
                 Soma:   18

    A resposta correta é 18.

 [+] Pelo sucesso no jogo anterior, o evento pediu novamente a sua ajuda
    para, dada uma sequência de números, calcular qual a maior soma de cartas
    possível no jogo.
 
 [+] O limite de tempo para cada resposta é de 3 segundos. 

 [+] Para começar, digite start: start
      Iniciando...

 [+] Desafio 1 - (L): [7, 1, 2, 4, 10, 2]
     A resposta é: 21
 [+] Correto!
 ```

## Execução
```
$ python2.7 hackaflag.py
```

## Flag
```
HACKAFLAG{g00d_CArd$_f0r_fl4GS}
```

BY : flavianogjc