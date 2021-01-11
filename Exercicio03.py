# Feito por: Ronyeri Marinho
#
# QUESTÃO 03 - A quantidade de dias dos meses variam de 28 a 31. Você deve criar um programa que receba
# o nome de um mês. Logo depois, deve-se exibir a quantidade de dias do mês inserido. 
# Obs: exiba “28 ou 29 dias” para Fevereiro.

# JANEIRO, MARCO, MAIO, JULHO, AGOSTO, OUTUBRO, DEZEMBRO = 31
# FEVEREIRO = 28 OU 29
# ABRIL, JUNHO, SETEMBRO, NOVEMBRO = 30

meses31Dias = ["JANEIRO", "MARÇO", "MAIO", "JULHO", "AGOSTO", "OUTUBRO", "DEZEMBRO"]
meses30Dias = ["ABRIL", "JUNHO", "SETEMBRO", "NOVEMBRO"]

mes = input("Digite o nome de um mês: ")

if mes.upper() in meses31Dias:
    print(mes, "tem 31 dias!")

elif mes.upper() in meses30Dias:
    print(mes, "tem 30 dias!")

elif mes.upper() == "FEVEREIRO":
    print(mes, "tem 28 ou 29 dias!")