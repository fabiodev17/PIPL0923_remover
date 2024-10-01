'''
#Comentário de uma linha


#Comentário 
#várias 
#linhas
'''

#prt
print("Hello World!")


#var
nome = "Valor" # String
idade = 10 # max int em c -> 2,147,483,647; max int -> não existe
nota = 10.9 # Float (6 a 7) e Double (14)
aprovado = True # 

print(nome)
nome = 10
print(nome)


soma = idade + 3
print(soma)


soma2 = nota + 2
print(soma2)


nome = "Valor"
soma3 = nome + "Foo"
print(soma3)


nome = "Valor"
#Não se pode somar Strings com inteiros
#soma4 = nome + 2024
#print(soma4)

op5 = nome * 2
print(op5)

#Print v2


nome = "Gonçalo"
ano = 2024

#Olá mundo, Gonçalo em 2024

#str(ano) converte para string

print("Olá Mundo, " + nome + " em " + str(ano))

print("Olá Mundo,", nome, "em", str(ano))

print("Olá Mundo,", nome, "em", ano)

print(f"Olá Mundo, {nome} em {ano}")



#-> % <-


op2 = 10 % 3
print(op2)

op2 = 12 % 3
print(op2)

op2 = 10/3
print(op2)

op2 = 10 // 3
print(op2)

#Ler dados do teclado
nome2 = input("Digite o seu nome: ")
print(f"ola, {nome2}")

print("--" * 10)
#Ifs


idade = 18
if (idade > 18):
    print("Adulto")
else:
    print("Não adulto.")


print("Fora dos Ifs")


idade = 10

if idade > 18:
    print("Adulto")
elif idade > 11:
    print("Jovem")
else:
    print("Criança")

num1 = float(input("Insere o primeiro número: "))
num2 = float(input("Insere o segundo número: "))

soma = num1 + num2

print("A soma dos dois números é:", soma)
