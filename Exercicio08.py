# Feito por: Ronyeri Marinho 
#
# QUESTÃO 08 - No Brasil, as cédulas são representadas por animais que estão em extinção na
# fauna do país. Assim, a tabela a seguir exibe os valores das cédulas e os animais
# correspondentes:

# >>>> AQUI VEM UMA TABELA <<<<

# Escreva um programa que receba um valor em reais (sem centavos) e indique
# quantos animais de cada espécie o usuário irá carregar no bolso, de forma que se
# tenha o mínimo de cédulas possível. Ex: R$ 32,00 →1 nota de R$ 20, 1 nota de R$
# 10 e uma nota de R$ 2, que resulta em Um mico-leão, uma arara e uma tartaruga
# de pente.

valor = int(input("Digite o valor em reais: R$ "))
total = valor
cedula = 200
totalCedulas = 0
animal = "Lobo-Guará"
while True:
    if total >= cedula:
        total -= cedula
        totalCedulas += 1

    else:

        if totalCedulas > 0:
            print(f"TOTAL DE {totalCedulas} CÉDULAS DE R${cedula}, EQUIVALENTES A {totalCedulas} {animal}")

        if cedula == 200:
           animal = "Garoupa"
           cedula = 100
        
        elif cedula == 100:
            animal = "Onça-Pintada"
            cedula = 50
        
        elif cedula == 50:
            animal = "Mico-Leão-Dourado"
            cedula = 20
        
        elif cedula == 20:
            animal = "Arara"
            cedula = 10
        
        elif cedula == 10:
            animal = "Garça"
            cedula = 5
        
        elif cedula == 5:
            animal = "Tartaruga de Pente"
            cedula = 2
        
        totalCedulas = 0
        if total == 0:
            break
