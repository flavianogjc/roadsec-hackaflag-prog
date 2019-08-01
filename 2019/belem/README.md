# HACKAFLAG Belém 2019
```
                           +++    Pense Bem++   +++ 

 [+] Muuuito antigamente, a TECTOY tinha um brinquedo chamado Pense Bem e ele 
     tinha um jogo para estimular a lógica das crianças chamado Adivinhe o
     Número. O jogo te dava 10 chances para tentar acertar um número de 0 a 100
     e sempre que você errava, ele informava se o número correto era maior ou
     menor que o palpite dado.

 [+] Baseado nesse jogo, que é muito fácil, o Hackaflag resolveu disponibilizar 
     uma versão mais desafiadora dele. Ele funciona da seguinte forma: o
     computador agora escolhe dois números (X e Y) e você pode fazer até 100
     perguntas para ele, com o objetivo de obter informações sobre esses dois
     números.

 [+] Já as perguntas funcionam da seguinte maneira: você envia dois
     números (A e B), no seguinte formato 'pergunta A B', e o computador irá
     responder com -1, 0 ou 1, segundo as seguintes regras:
       
      -1 se (A XOR X)  >  (B XOR Y)
       0 se (A XOR X) ==  (B XOR Y)
       1 se (A XOR X)  <  (B XOR Y)

 [+] No momento em que você souber a resposta, antes do término das 100
     perguntas, o formato da resposta é o seguinte: 'resposta C D'.

 [+] O tempo para jogar cada partida é de 37 segundos.
 
 [+] Para começar, digite start: start
     Iniciando...
 [+] Partida 1 \ 10 - Número entre [0, 10]
 [+] Movimento 1: pergunta 0 0
 [+] Comparação: 1
 ```

## Execução
```
$ python2.7 hackaflag.py
```

## Flag
```
HACKAFLAG{JUZVGVCSGMQGIMBAKAZW4UZUJUZW45BQEBWMHM2HGFRTAIJB}
```

BY : flavianogjc