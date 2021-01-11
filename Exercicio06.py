# Feito por: Ronyeri Marinho
#
# QUESTÃO 06 - A tabela a seguir lista níveis de sons em decibéis para vários barulhos comuns:
#
#   CAUSA                    DECIBÉIS
# Britadeira                   130
# Cortador de Grama            106 
# Despertador                  70
# Sala Tranquila               40
#
# Escreva um programa que leia um nível de som em decibéis e se este for
# exatamente igual a algum dos níveis mostrados na tabela exiba o nome do que
# causa este barulho. Caso o valor esteja entre dois destes níveis, exiba entre quais
# quais destes barulhos o nível se encontra. Ex: 115 dB está entre o barulho de um
# cortador de grama a gás e uma britadeira.
# Caso, o nível esteja abaixo do menor valor da tabela e acima do maior valor, exiba
# mensagens adequadas indicando estes fatos.

somDecibeis = int(input("Digite o nível de som em decibéis: "))

if somDecibeis == 130:
    print("SOM DE BRITADEIRA!")

elif somDecibeis == 106:
    print("SOM DE CORTADOR DE GRAMA A GÁS!")

elif somDecibeis == 70:
    print("SOM DE DESPERTADOR!")

elif somDecibeis == 40:
    print("SOM DE SALA TRANQUILA")

elif somDecibeis < 130 and somDecibeis > 106:
    print("O SOM ESTÁ ENTRE O BARULHO DE UMA BRITADEIRA E UM CORTADOR DE GRAMA A GÁS!")

elif somDecibeis < 106 and somDecibeis > 70:
    print("O SOM ESTÁ ENTRE O BARULHO DE UM CORTADOR DE GRAMA A GÁS E UM DESPERTADOR!")

elif somDecibeis < 70 and somDecibeis > 40:
    print("O SOM ESTÁ ENTRE O BARULHO DE UM DESPERTADOR E UMA SALA TRANQUILA!")

else:
    print("O valor inserido em decibéis não se enquadra aos barulhos disponíveis!")