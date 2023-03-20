# Casting

# Convertem tipos de dados numericos e de texto em outros dados do tipo de numeros ou texto
"""
  Sem alterações no tipo de dado:
  x = 2    int 
  y = 2.8  float 
  z = '2'   str
"""
# Exemplos a baixo alterando o tipo de dado para int:

x = int(2)
y = int(2.8)
z = int('2')

print(x,y,z)
# Imprimindo para ver as tranformações dos tipos de dados em int


#float

a =  float(2.3)
b =  float(2)      # 2 int recebeu float 2.0
c =  float('2.3')   
d =  float('2')    # 2 str recebeu float 2.0
print(a,b,c,d)
# Tranformamos todos os tipos em float


# String

t = str('s1')
r = str(2)
z = str(2.3)

# Checando as alterações usando type
print("A variável t é do tipo ",type(t))
print("A variável r é do tipo ",type(r))
print("A variável z é do tipo ",type(z))



# Tipo de dado String
k = 'A'
print(k)
print('K é do tipo: ',type(k))
# Tipo String aqui



# Ao imprimirmos o código abaixo dará um erro
# Pois estamos tentanto transformar uma str('Texto , letra' em um tipo int)
"""
k = int('A')
print(k)
print('K é do tipo: ',type(k))
# Não conseguimos alterar um dado string("textp,letra") em um int 
"""


#English

# casting

# Convert numeric and text data types to other text or number data types
"""
  No data type changes:
  x = 2 int
  y = 2.8 float
  z = '2' str
"""
# Examples below changing the data type to int:

x = int(2)
y = int(2.8)
z = int('2')

print(x,y,z)
# Printing to see transformations of data types in int


#float

a = float(2.3)
b = float(2) # 2 int received float 2.0
c = float('2.3')
d = float('2') # 2 str received float 2.0
print(a,b,c,d)
# Convert all types to float


# String

t = str('s1')
r = str(2)
z = str(2.3)

# Checking for changes using type
print("The variable t is of type ",type(t))
print("The variable r is of type ",type(r))
print("Variable z is of type ",type(z))



# String data type
k = 'A'
print(k)
print('K is of type: ',type(k))
# Type String here



# When we print the code below it will give an error
# Because we are trying to transform a str('Text, letter' into an int type)
"""
k = int('A')
print(k)
print('K is of type: ',type(k))
# We can't change a given string("textp,letter") into an int
"""