# HACKAFLAG Vitória 2017
```
                   +++    HACKAFLAG - Programação     +++

 [+] Todo Roadsec conta com os mais diversos palestrantes de todo o
     território nacional. Uma das decisões da organização do evento é que, 
     em cada palestra, deverá ter sempre um staff acompanhando um determinado
     palestrante durante toda a sua apresentação, para resolver problemas
     logísticos, técnicos, e o que mais puder aparecer para manter o bom
     andamento do evento.

     Como sempre há mais palestrantes que staffs, a organização pediu sua ajuda
     para saber de quantas formas diferentes é possível arranjar staffs e
     palestrantes para um determinado evento, de forma que todos os staffs
     acompanhem no mínimo um palestrante durante a sua apresentação.

 [+] Dessa forma, dados dois naturais P e S, você deverá informar de
     quantas maneiras diferentes é possível combinar palestrantes e staffs, de
     forma que cada staff acompanhe no mínimo um palestrante.

 [+] Como o resultado pode ser muito grande, você deverá responder com o
     resto da divisão da sua resposta pelo valor 2^31 - 1. Segue um exemplo
     utilizando a operação de resto para os valores de P = 3 e S = 2:

        P = (p1, p2, p3)
        S = (s1, s2)

        1: p1-s1, p2-s1, p3-s2
        2: p1-s1, p2-s2, p3-s2
        3: p1-s1, p2-s2, p3-s1
        4: p1-s2, p2-s1, p3-s1
        5: p1-s2, p2-s2, p3-s1
        6: p1-s2, p2-s1, p3-s2
        ______________________
                             6  % 2 ^ 31 - 1 = 6

    A resposta correta é 6.

 [+] O limite para cada resposta será de 3 segundos.
 
 [+] Para começar, digite start: start
      Iniciando...

 [+] Teste 1 - (P, S): 5, 3
     A resposta é: 150
 [+] Correto!
 ```

## Execução
```
$ python2.7 hackaflag.py
```

## Flag
```
HACKAFLAG{pr3f1r0_PAl3str4r}
```

BY : flavianogjc