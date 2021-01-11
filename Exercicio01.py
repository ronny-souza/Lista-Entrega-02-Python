# Feito por: Ronyeri Marinho
#
# QUESTÃO 01 - Escreva um programa que leia um inteiro do usuário. Depois, seu programa deve exibir
# uma mensagem indicando se o inteiro é par ou ímpar.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par!")
else:
    print("O número é ímpar!")