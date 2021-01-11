# Feito por: Ronyeri Marinho
#
# QUESTÃO 05 - Escreva um programa que determine o nome de uma forma geométrica a partir do número de lados.
# Seu programa deve dar suporte a qualquer forma que contenha no mínimo 3 e no máximo 10 lados. 
# Se o número de lados estiver abaixo ou acima deste limite, deve ser exibida uma mensagem de erro apropriada.


quantidadeLados = int(input("Digite a quantidade de lados existentes na forma geométrica: "))

if quantidadeLados == 3:
    print("TRIÂNGULO!")

elif quantidadeLados == 4:
    print("QUADRILÁTERO!")

elif quantidadeLados == 5:
    print("PENTÁGONO!")

elif quantidadeLados == 6:
    print("HEXÁGONO!")

elif quantidadeLados == 7:
    print("HEPTÁGONO!")

elif quantidadeLados == 8:
    print("OCTÓGONO!")

elif quantidadeLados == 9:
    print("ENEÁGONO!")

elif quantidadeLados == 10:
    print("DECÁGONO!")

else:
    print("Erro: Só é permitido formas com o mínimo de 3 lados e o máximo de 10!")