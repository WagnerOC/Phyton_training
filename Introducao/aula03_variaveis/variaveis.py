#Variáveis:

# Servem para armazenarem valores de dados
# Python não tem comando para declarar uma variável, usando var como exemplo , ex: var = 2
# A variável é criada no momento que você atribui valor a ela

# Atribuindo uma variável
# x = 5    Aqui x está recebendo 5
# y = 1+2   y está recebendo uma soma de 1 + 2
# w = 'Ana' w está recebendo uma String(dado do tipo texto)
# Nunca devemos falar que x é igual a 5 por exemplo

# Variáveis não podem começar com números
# Variáveis não podem ter espaçamentos, Ex: numero 1
# Variáveis podem ter _ para separar,Ex: numero_1 começar com letra maiúsculas ou minúsculas
# Indicado que comece com letras minúsculas
# Indicado que use em vez de _ letras maiúsculas para separar no nome de uma variável, Ex:sucoLaranja

# Podemos atribuir vários valores as variáveis
# Ex: h, j, l = 1, 3 , 5     assim mesmo, em uma linha
# h = 1                      h recebeu o valor 1
# j = 3                      j recebeu o valor 3
# l = 5                      l recebeu o valor 5

h, j, l = 1, 3, 5

# imprimindo separadas
print(h)
print(j)
print(l)

# ou todas juntas
print(h,j,l)


# Podemos atribuir a varias variáveis o mesmo valor
a = b = c = 'Python'

# Todas as variáveis estão com o mesmo valor
print(a)
print(b)
print(c)

#  Podemos unir duas variáveis usando uma variável para recebe-las
# Ex: h = w + a
# h recebeu Ana + Python que estão nas variáveis w e a
d = 'Ana'
a = ' faz curso de Python3'
# usamos um espaço antes de 'faz', para dar o espaçamento entre as variáveis
e = d + a
print(e)

# Perceba que primeiramente, 'a' tinha recebido o valor 'Python' a cima
# Depois trocamos seu valor para ' faz curso ..'
# Podemos trocar os valores de uma variável, e isso deve ser tratado com cuidado


# Operadores matemáticos:

# Para somar dois números +
f = 5
g = 3
h = 5 + 3
print('A soma de',f,'+',g,' é igual a ',h)
# Percebe que ao imprimir podemos usar strings junto com as variáveis

# Atributos de Contas:
#  - Subtração      h = 5 - 3
#  / divisão        h = 5 / 3
#  * multiplicação  h = 5 * 3
#  % módulo         h = 5 % 3  

# Não podemos atribuir uma concatenação entre uma variável que recebe um número com uma que tenha recebido uma String
# Ex: a = 'Ana'   b = 5   c = a + b
# Ao imprimir c, aparecerá um erro
# Pois  Python é uma linguagem dinâmica e fortemente tipada
# Dinâmica pois não é estática, a variável pode ter seu valor alterado
# Tipada, pois não podemos usar uma var do tipo numero com uma do tipo texto


 
#English:

#Variables:

# Serve to store data values
# Python has no command to declare a variable, using var as an example, ex: var = 2
# The variable is created the moment you assign a value to it

# Assigning a variable
# x = 5 Here x is getting 5
# y = 1+2 y is getting a sum of 1 + 2
# w = 'Ana' w is receiving a String (text type data)
# We should never say that x is equal to 5 for example

# Variables cannot start with numbers
# Variables cannot have spaces, eg number 1
# Variables can have _ to separate, Ex: number_1 start with uppercase or lowercase letter
# Indicated that it starts with lowercase letters
# Indicated that you use _ instead of capital letters to separate the name of a variable, Ex: orange juice

# We can assign multiple values ​​to variables
# Ex: h, j, l = 1, 3 , 5 like that, in one line
# h = 1 h received the value 1
# j = 3 j received the value 3
# l = 5 l received the value 5

h, j, l = 1, 3, 5

# printing separately
print(h)
print(j)
print(l)

# or all together
print(h,j,l)


# We can assign multiple variables the same value
a = b = c = 'Python'

# All variables have the same value
print(a)
print(b)
print(c)

# We can join two variables using a variable to receive them
# Eg: h = w + a
# h received Ana + Python which are in variables w and a
d = 'Anna'
a = ' take a Python3 course'
# we use a space before 'makes', to give the spacing between the variables
e = d + a
print(e)

# Notice that first, 'a' had received the 'Python' value above
# Then we change its value to ' take a course ..'
# We can swap the values ​​of a variable, and this should be handled with care


# Mathematical operators:

# To add two numbers +
f = 5
g = 3
h = 5 + 3
print('The sum of',f,'+',g,' is equal to ',h)
# Realize that when printing we can use strings together with the variables

# Attributes of Mathematical Accounts:
# - Subtraction h = 5 - 3
# / division h = 5 / 3
# * multiplication h = 5 * 3
# % modulus h = 5 % 3

# We cannot assign a concatenation between a variable that receives a number with one that has received a String
# Ex: a = 'Ana' b = 5 c = a + b
# When printing c, an error will appear
# Because Python is a dynamic and strongly typed language
# Dynamic because it is not static, the variable can have its value changed
# Typed, because we cannot use a var of type number with one of type text