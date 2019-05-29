# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

#print("\n******************* Python Calculator *******************\n")
#print=("1 - Soma 2 - Subtração\n3 - Multiplicação\n4 - Divisão\nDigite 5 para sair.")

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

op=0
while op!=5:
    op = int(input("Digite a opção desejada: "))
    if (op == 1):
        x=float(input("Digite o primeiro número: "))
        y=float(input("Digite o segundo número: "))
        print("O resultado da soma de {} e {} é {}\n".format(x,y,add(x, y)))

    if (op==2):
        x=float(input("Digite o primeiro número: "))
        y=float(input("Digite o segundo número: "))
        print("O resultado da subtração de {} e {} é {}\n".format(x, y, sub(x, y)))

    if (op==3):
        x=float(input("Digite o primeiro número: "))
        y=float(input("Digite o segundo número: "))
        print("O resultado da multiplição de {} e {} é {}\n".format(x, y, mul(x, y)))

    if (op==4):
        x=float(input("Digite o primeiro número: "))
        y=float(input("Digite o segundo número: "))
        print("O resultado da divisão de {} e {} é {}\n".format(x, y, div(x, y)))