#tarefa estrutura sequencial
import math
# Ex01 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.

print("\nAlô mundo\n")

# Ex02 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

num = input("\nInsira um número: \n")
print("\nO número informado foi: ", num)

# Ex03 - Faça um Programa que peça dois números e imprima a soma.

num1 = float(input("\nInsere o primeiro número: \n"))
num2 = float(input("\nInsere o segundo número: \n"))

soma = num1 + num2

print("\nA soma dos dois números é: ", soma)

# Ex04 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("\nInsira a primeira nota: \n"))
nota2 = float(input("\nInsira a segunda nota: \n"))
nota3 = float(input("\nInsira a terceira nota: \n"))
nota4 = float(input("\nInsira a quarta nota: \n"))
media = (nota1 + nota2 + nota3 + nota4) / 4
print("\nA média das notas é: ", media)

# Ex05 - Faça um Programa que converta metros para centímetros.

metros = float(input("\nInsira o valor em metros: \n"))
centimetros = metros * 100
print(metros, "\nMetros equivalem a", centimetros, "centímetros\n")

# Ex06 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input("\nInsira o raio do círculo: \n"))
area = math.pi * (raio ** 2)
print("\nA área do círculo é: ", area)

# Ex07 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("\nInsira o tamanho do lado do quadrado: \n"))
area = lado ** 2
dobro_area = area * 2
print("\nA área do quadrado é: ", area)
print("\nO dobro da área do quadrado é: ", dobro_area)

# Ex08 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

horas_valor = float(input("\nInsira quanto ganha por hora: \n"))
horas_trabalhadas = float(input("\nQuantas horas trabalha por mês: \n"))
salario = horas_valor * horas_trabalhadas
print("\nNo fim do mês irá receber: ", salario,"€")

# Ex09 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahrenheit = float(input("Insira a temperatura em Fahrenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9)
print("A temperatura em Celsius é:", celsius)

# Ex10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius1 = float(input("Insira a temperatura em Celsius: "))
fahrenheit1 = (celsius1 * 9/5) + 32
print("A temperatura em Fahrenheit é:", fahrenheit1)

# Ex11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

num1 = int(input("Insira o primeiro número inteiro: "))
num2 = int(input("Insira o segundo número inteiro: "))
num3 = float(input("Insira um número real: "))

#11.a
resultado1 = (2 * num1) * (num2 / 2)
#11.b
resultado2 = (3 * num1) + num3
#11.c
resultado3 = num3 ** 3

print("O produto do dobro do primeiro com metade do segundo é:", resultado1)
print("A soma do triplo do primeiro com o terceiro é:", resultado2)
print("O terceiro número elevado ao cubo é:", resultado3)

# Ex12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Insira a sua altura em metros: "))
peso_ideal = (72.7 * altura) - 58
print("O seu peso ideal é:", peso_ideal, "kg")

# Ex13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal.

altura = float(input("Insira a sua altura em metros: "))
sexo = input("Insira o sexo (M para masculino, F para feminino): ")

if sexo.upper() == 'M':
    peso_ideal = (72.7 * altura) - 58
elif sexo.upper() == 'F':
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Sexo inválido. Insira M ou F.")
    peso_ideal = None

if peso_ideal:
    print("O seu peso ideal é:", peso_ideal, "kg")