# Feito por: Ronyeri Marinho
#
# QUESTÃO 02 - É comumente dito que 1 ano humano é equivalente a 7 anos caninos. Porém, esta simples 
# conversão falha em reconhecer que cães alcançam a vida adulta com aproximadamente 2 anos de idade.
# Como resultado disso, acredita-se que é melhor contar cada um dos dois primeiros anos humanos
# como 10.5 anos caninos, e após isso, contar cada ano humano adicional como 4 anos caninos.

# Escreva um programa que receba o valor de anos humanos e implemente a conversão para anos caninos de
# acordo com a descrição dada anteriormente. Certifique-se de que seu programa trabalhe corretamente para
# conversões de menos de dois anos humanos, bem como para conversões de dois ou mais anos humanos.
# Seu programa deve descrever um erro apropriado, caso o usuário entre com um número negativo.

anosHumanos = float(input("Digite o valor da idade em anos humanos: "))
anosCaninos = 0.0

if anosHumanos <= 2.0 and anosHumanos > 0 :

    anosCaninos += 10.5
    print(anosHumanos, "anos humanos equivalem a", anosCaninos, "anos caninos")

elif anosHumanos > 2.0:

    # soma os 10.5 equivalentes aos 2 primeiros anos
    anosCaninos += 10.5
    # remove os 2 primeiros anos humanos para não influenciar no resto
    anosHumanos -= 2.0
    # multiplica o que sobrou dos anos humanos por 4
    anosCaninosAdicionais = anosHumanos * 4
    # soma os anos caninos ao resultado da multiplicação
    anosCaninos += anosCaninosAdicionais
    # traz de novo os 2 anos que foram removidos antes, para que a impressão do valor saia correta
    anosHumanos += 2.0
    print(anosHumanos, "anos humanos equivalem a", anosCaninos, "anos caninos")

elif anosHumanos < 0.0:
    print("Erro: Não é possiível utilizar números negativos para o cálculo!!")

