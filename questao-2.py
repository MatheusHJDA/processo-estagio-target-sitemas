#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def verifica_fibonacci(numero):

    fibonacci = [0, 1]

    while fibonacci[-1] < numero:
        proximo_valor = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo_valor)

    if numero in fibonacci:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

try:
    numero = int(input("Hello world, digite um número para verificar se pertence à sequência de Fibonacci: "))
    print(verifica_fibonacci(numero))
except ValueError:
    print("Coloque um número inteiro por favor....")

