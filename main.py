def q1():
    """
    Faça um programa que calcula a
    quantidade de divisores de um
    número (incluindo 1 e o próprio 
    número) que são divisíveis por 3.
    """
    numero = int(input("Digite um número")) # 4
    # os divisores deste 'numero'
    # 4: 1,2,3,4
    for i in range(1, numero + 1):
        if (numero % 1 == 0):
            print(1)






    numero = int(input(""))
    quantidade_divisores = 0
    for i in range(2, numero+1):
        if numero % i == 0 and i % 3 == 0:
            quantidade_divisores += 1
    if quantidade_divisores == 0:
        print("O número não possui divisores multiplos de 3")
    else:
        print(
            f"Quantidade de divisores divisiveis por 3: {quantidade_divisores}")

def q2():

    num1 = int(input("Digite o numero 1"))
    num2 = int(input("Digite o numero 2"))

    if num1 > num2:
        temp = num1
        num1 = num2
        num2 = temp

    soma = 0
    for i in range(num1, num2):
        if i > 0:
            soma += 1
    print(soma)

def q3():

    qnt, soma, nota = 0, 0, 0
    while True:
        nota = int(input("Digite uma nota: "))

        if nota == -1:
            break

        if nota in range(0,11):
            soma += nota
            qnt += 1
        else:
            print("Valor da nota está fora do intervalo.")

    media = soma / qnt
    
    print(f"A média das notas foi {media}")