# Feito por: Ronyeri Marinho
#
# QUESTÃO 04 - Os computadores apenas armazenam informação em valores que estão
# codificados em código binário, em formato de zeros e uns. Para se codificar um
# texto, é necessário que se adote um valor binário para cada caracter, letra ou
# número do alfabeto. O código mais simples utilizado em sistemas computacionais é
# o código ASCII (Sigla de American Standard Code for Information Exchange), que
# está representada na imagem a seguir. Perceba que cada caracter tem sua
# representação em Decimal (no caso é um valor inteiro), Hexadecimal e a sua
# visualização como caracter. Sabendo que existe no Python a função ord() que
# converte um caracter em sua representação decimal, crie um programa que receba
# uma letra do alfabeto, e indique se esta letra é maiúscula ou minúscula. Você deve
# utilizar as informações da tabela ASCII para resolver esta questão. A seguir está
# uma forma de uso da função ord().

caracter = input("Digite uma letra do alfabeto: ")

if caracter.isupper():
    print("Letra digitada está em MAIÚSCULA!")
    caracterASCII = ord(caracter)
    print("Representação decimal da letra: ", caracterASCII)

else:
    print("Letra digitada está em MINÚSCULA!")
    caracterASCII = ord(caracter)
    print("Representação decimal da letra: ", caracterASCII)