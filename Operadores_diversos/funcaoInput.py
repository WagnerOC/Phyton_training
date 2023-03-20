"""
Funcao input() - Função para receber dados do usuário
"""
#Existem várias formas de armazenar os dados do usuário

print('Qual é o seu nome?')
nome = input()
print(nome)

#Pode ser assim
nome = input('Qual é o seu nome ? ')
idade = input('Qual é a sua idade? ')
print("Olá"+nome+",sua idade é"+idade)

#pode ser assim
print("Seu nome é: {0} e sua idade é: {1}".format(nome,idade))
# a numeração das chaves, segue a mesma ordem das variáveis

#pode ser assim
nome = input('Qual é o seu nome ? ')
idade = input('Qual é a sua idade? ')

print(f'Seu nome é: {nome} e sua idade é:{idade}')






#English
"""
Function input() - Function to receive data from the user
"""
# There are several ways to store user data

print('What is your name?')
name = input()
print(name)

#Can it be like this
name = input('What is your name? ')
age = input('What is your age? ')
print("Hello"+name+",your age is"+age)

#can it be like this
print("Your name is: {0} and your age is: {1}".format(name,age))
# the numbering of the keys follows the same order as the variables

#can it be like this
name = input('What is your name? ')
age = input('What is your age? ')

print(f'Your name is: {name} and your age is:{age}')