# HACKAFLAG Florianópolis 2017
```
                   +++    HACKAFLAG - Challenges     +++

 [+] Chegando a última edição do Hackaflag, todos os finalistas começaram  a 
     descobrir sob quais critérios eles estarão jogando cada uma das modalidades.

 [+] Uma das modificações do desafio individual é que não haverá limite de
     tempo para o término do torneio, e que vencerá a final aquele competidor
     que terminar primeiro todos os desafios.

 [+] A outra diferença, é que cada competidor receberá os desafios por
     lotes de pontuação, funcionando da seguinte maneira:
      - Serão quatro categorias de desafios (crypto, web, rev, e misc)
      - Os desafios estarão em uma pilha por categoria e deverão ser acessados
        do topo para a base
      - Cada desafio tem uma pontuação que varia de 0 a 9
      - Um competidor só poderá escolher um lote de challs do topo de cada
        pilha, de forma a somar um número múltiplo de 4 pontos.
      - Em um lote não pode haver mais do que um desafio de uma mesma categoria.
      - Um competidor terá acesso à pontuação de todos os desafios antes de
        realizar suas escolhas.
      - Vence aquele que conseguir resolver todos os seus lotes de desafios
        múltiplos de 4 pontos.

 [+] O primeiro questionamento dos competidores é o que aconteceria se um
     jogador não conseguisse formar um múltiplo de 4 no final dos lotes. Então,
     foi respondido os jogadores sempre receberão lotes válidos, e não conseguir
     implica em más escolhas feito pelo jogador porque você recebeu a
     incumbência de, dado um pacote de desafios, da base das pilhas para o topo,
     responder se é possível resolver seguindo as regras ou não.

 [+] Exemplo de pacote: [[4, 3, 0, 1], [0, 1, 3, 3], [1, 3, 5, 4]]
 
 [+] Exemplo de resolução:
                                Escolha 1: crypto(1), web(3)
          1     3   5   4       Escolha 2: misc(4)
          0     1   3   3       Escolha 3: rev(5), misc(3)
          4     3   0   1       Escolha 4: crypto(0), web(1), rev(3)
        crypto web rev misc     Escolha 5: crypto(4), web(3), rev(0), misc(1)
       (desafios empilhados)    (Todas as pilhas vazias, foi possível resolver)

 [+] Dessa forma, responda com 1, se for possível resolver o pacote, e 0
     caso contrário. 
 
 [+] O limite de tempo para cada resposta é de 7 segundos. 
 
 [+] Para começar, digite start:
      Iniciando...

 [+] Desafio 1 - (Challs): [[3, 4, 0, 1], [4, 3, 2, 4], [2, 3, 0, 3]]
     A resposta é: 0
 [+] Correto!
 ```

## Execução
```
$ python2.7 hackaflag.py
```

## Flag
```
HACKAFLAG{e_4IndA_pr3C1sa_MaTAr_4$_flags}
```

BY : flavianogjc