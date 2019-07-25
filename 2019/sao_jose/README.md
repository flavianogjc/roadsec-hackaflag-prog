# HACKAFLAG São José 2019
```
                            +++   HACKACOINS   +++

 [+] Você foi contratado para trabalhar na nova moeda desenvolvida para o
     Hackaflag, chamada de Hackacoin - Criptomoeda do Hackaflag.

 [+] Sua primeira tarefa é implementar o funcionamento do UTXO (Unspent
     Transaction Outputs) que é o protocolo responsável por identificar no
     blockchain quem ainda tem saldo na rede ou não.

 [+] A ideia principal do UTXO é que uma carteira não possui um valor total em
     conta, mas sim uma lista valores oriundos de diferentes transações na rede
     que, ao serem somados, resultam no saldo de uma carteira observada. Quando
     uma transação é realizada, o protocolo é responsável por receber o valor,
     verificar na lista um conjunto de valores que resulte no mínimo o valor da
     transação e, assim, validar o pagamento.

 [+] Para diferir do Bitcoin, você foi incumbido de diferenciar o UTXO da
     seguinte forma: ao invés de retornar apenas um conjunto de valores válidos,
     o UTXO irá receber a lista de valores de entrada e um intervalo, e irá
     responder de quantas formas diferentes os valores da lista podem ser
     combinados para resultar em um valor dentro do intervalo.

 [+] Exemplo:

 Carteira:          [1, 3, 5, 7, 9]
 Intervalo:         [8, 10]
 Conjuntos válidos: [(9), (1, 7), (1, 9), (3, 5), (3, 7), (1, 3, 5)]

 Resposta:          6

 [+] O limite para cada resposta é de 3 segundos.

 [+] Para começar, digite start: start
     Iniciando...

 [+] Carteira 1/50:
     Valores: [1, 3, 5, 7, 9]
     Intervalo: [8, 10]
     A resposta é: 6
 [+] Acertô, miseravi!
 ```

## Execução
```
$ python2.7 hackaflag.py
```

## Flag
```
HACKAFLAG{NZQW65DFNVXXK5DSMFTGYYLH}
```

BY : flavianogjc