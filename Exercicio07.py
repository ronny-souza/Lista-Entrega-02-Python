# Feito por: Ronyeri Marinho
#
# QUESTÃO 07 - O ano é dividido em quatro estações: primavera, verão, outono e inverno. De
# forma geral o calendário das estações está na tabela a seguir:
#
# Estação:          Data
# Primavera         22 de Setembro
# Verão             21 de Dezembro
# Outono            20 de Março
# Inverno           21 de Junho
#
# Crie um programa que leia o mês (nome do mês) e o dia. O programa deve exibir
# qual a estação associada à data inserida.

meses = ["SETEMBRO", "DEZEMBRO", "MARÇO", "JUNHO"]

mes = input("Digite o mês: ")
dia = int(input("Digite o dia: "))

if mes.upper() == meses[0] and dia == 22:
    print("Primavera!")

elif mes.upper() == meses[1] and dia == 21:
    print("Verão!")

elif mes.upper() == meses[2] and dia == 20:
    print("Outono!")

elif mes.upper() == meses[3] and dia == 21:
    print("Inverno!")

else:
    print("Digite o mês e o dia correspondentes a alguma estação!!")