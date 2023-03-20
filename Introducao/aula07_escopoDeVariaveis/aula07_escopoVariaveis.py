# Escopo de variáveis

# variáveis globais
# Acessiveis em qualquer lugar do código
# Se reescrevermos a variável com outro valor, ela receberá esse outro valor

#variáveis locais
# declaradas dentro de um bloco de uma função
# Não podem ser alteradas ou usadas por outras funções
# Só existe quando a função está sendo executada

x = 5

def funcao():
    x = 3
    print("O valor da variável local: ", x)

funcao()
print('O valor da variável global: ', x)  

y = 'Gabriel'         #nome
z = 1.74              #altura
t = "000.000.000-00"  #cpf
l = 23                #idade

# Sempre é importante colocar nomes em suas variáveis
# Colocar nome explícito
# Para que exista significância
# Ex:

# nome = 'Gabriel'
# altura = 1.74
# cpf = "000.000.000-00"
# idade = 23


#English

# Scope of variables

# global variables
# Accessible anywhere in the code
# If we rewrite the variable with another value, it will receive that other value

# local variables
# declared inside a function block
# Cannot be changed or used by other functions
# Only exists when the function is being executed

x = 5

def function():
    x = 3
    print("The value of the local variable: ", x)

function()
print('The value of the global variable: ', x)

y = 'Gabriel' #name
z = 1.74 #height
t="000.000.000-00" #cpf
l = 23 #age

# It is always important to name your variables
# Put explicit name
# For there to be significance
# Ex:

# name = 'Gabriel'
# height = 1.74
# cpf = "000.000.000-00"
# age = 23