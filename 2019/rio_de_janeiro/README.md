# HACKAFLAG Rio de Janeiro 2019
```
                              +++    DDoS   +++ 

 [+] Essa semana, o site do Hackaflag estava muito instável e alguns jogadores 
     estavam reclamando não estar conseguindo acessar nem a plataforma e  nenhum
     dos servidores de desafios. Após as reclamações, Boot resolveu pegar o
     relatório de quantidade de acessos e verificar o que realmente estava
     acontecendo com o servidores.

 [+] Os relatórios do serviço de provisionamento vem em uma lista, informando a 
     quantidade de conexões a cada segundo do intervalo observado.

 [+] Por isso, Boot resolveu checar o serviço da seguinte forma: se a quantidade
     total de conexões em um intervalo t for maior que esse intervalo vezes a
     cota c contratada, isso é configurado como um DDoS.

 [+] Assim, Boot pediu a sua ajuda para verificar, baseado no relatório, qual o 
     maior intervalo de tempo em que o ocorreu DDoS no servidor.

 [+] Exemplo:
     Lista   : [1, 2, 1, 11, 11, 5, 3, 1]
     Cota    : 10
     Resposta: 2

 [+] O limite para cada resposta é de 2 segundos.
 
 [+] Para começar, digite start: start
     Iniciando...

 [+] Relatório 1/50: 
     Acessos: [1, 2, 1, 11, 11, 5, 3, 1]
     Cota: 10
     A resposta é: 2
 [+] Acertô, miseravi!
 ```

## Execução
```
$ python2.7 hackaflag.py
```

## Flag
```
HACKAFLAG{IRCG6U2OIFHUMVKOINEU6TSBIFJVGSKN}
```

BY : flavianogjc