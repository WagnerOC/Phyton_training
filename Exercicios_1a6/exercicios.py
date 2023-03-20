"""
Exercícios - Python

Observação: Todos os exercícios devem
utilizar a função input, de forma que
o usuário possa determinar os dados de
entrada.

01 - área de um retângulo
02 - área de um quadrado
03 - Se o produto que você quer avaliar
custa (??) reais, qual será o valor
do mesmo com desconto de (??)%
04 - área de um círculo
05 - conversão de reais para dolar
06 - conversão de dolar para reais
"""


""" Exercício 01 - área do retângulo """

print('Calcule a área de um retângulo.')
base = input('Qual o tamanho da base do seu retângulo? ')
altura = input('Qual o tamanho da altura do seu retângulo? ')
area = float(base) * float(altura)

print(f'Do seu retângulo: a base é:{base}.E a altura é:{altura}.Portanto a área é:{area} unidades de medidas.')



""" Exercício 02 - área de um quadrado """

print('Calcule a área de um quadrado.')
lado = input('Qual o tamanho de um dos lados do seu quadrado? ')
areaQuadrado = float(lado) ** 2
print(f'A área do seu Quadrado é:{areaQuadrado}')



"""Exercício 03 - Se o produto que você quer avaliar custa (??) reais, qual será o valor do mesmo com desconto de (??)%"""

print('Calcule quantos reais irá pagar no produto, com a porcentagem de desconto que você viu na Loja.')
valorProduto = input('Qual o valor do produto que você quer? ')
desconto = input('A loja está dando quantos porcento de desconto? ')
valorDoDesconto = float(valorProduto) * (desconto/100)
produtoComDesconto = float(valorProduto) * (100 - desconto / 100)
print(f'Você irá pagar no produto com desconto de {desconto}porcento: R${produtoComDesconto}! O valor de desconto é de R${valorDoDesconto}')



"""04 - área de um círculo"""

print('Calcule a área do círculo')
raio = ('Qual o raio do circulo? ')
pi = 3.14
area = float(pi) * float(raio**2)
print(f'Como o raio do círculo é{raio}. A área do círculo é: {area}')



"""05 - Conversão de reais para dolar"""

print('Coverta o dinheiro Reais em dinheiro Dolar.')
reais = ('Digite quantos Reais você quer converter em Dolares: R$ ')
dolar = 5.28 # 1 dólar vale 5.28 reais
dolarConvert = float(reais) / float(dolar)
print(f'Como o $1.00 está{dolar} reais hoje, convertendo R${reais} em dólares, você terá: ${dolarConvert} dólares!')



"""06 - Conversão da moeda Dólar para a moeda Real"""

print('Coverta a moeda Dólar em moeda Real.')
dolar = ('Digite quantos Dólares você quer converter em Reais: $ ')
real = 0.19 #1 real vale 0,19 dólares 
realConvert = float(dolar) * float(real)
print(f'Como R$1.00 real está{real} dólares hoje, convertendo ${dolar} em dólares, você terá: R${realConvert} reais!')





# English

"""
Exercises - Python

Note: All exercises must
use the input function, so that
the user can determine the data of
Prohibited.

01 - area of a rectangle
02 - area of a square
03 - If the product you want to evaluate
costs (??) reais, what will be the value
of the same with a discount of (???)%
04 - area of a circle
05 - conversion from reais to dollars
06 - conversion from dollar to reais
"""

""" Exercise 01 - rectangle area """

print('Calculate the area of a rectangle.')
base = input('How big is the base of your rectangle? ')
height = input('How tall is your rectangle? ')
area = float(base) * float(height)

print(f'From your rectangle: the base is:{base}.And the height is:{height}.So the area is:{area} units of measurement.')



""" Exercise 02 - area of a square """

print('Calculate the area of a square.')
side = input('How long is one of the sides of your square? ')
areaSquare = float(side) ** 2
print(f'The areaSquararea of your Square is:{areaSquare}')



"""Exercise 03 - If the product you want to evaluate costs (??) reais, what will be its value with a discount of (??)%"""

print('Calculate how many reais you will pay for the product, with the discount percentage you saw in the Store.')
productValue = input('What is the price of the product you want? ')
discount = input('The store is giving how many percent discount? ')
discountValue = float(productValue) * (discount/100)
productWithDiscount = float(productValue) * (100 - discount / 100)
print(f'You will pay for the product with a {discount}percent discount: R${productWithDiscount}! The discount value is R${discountValue}')



"""04 - area of ​​a circle"""

print('Calculate the area of ​​the circle')
radius = input('What is the radius of the circle? ')
pi = 3.14
area = float(pi) * float(radius**2)
print(f'As the radius of the circle is {radius}. The area of the circle is: {area}')



"""05 - Conversion from reais to dollars"""

print('Convert the Reais money into Dollar money.')
reais = ('Type how many Reais you want to convert into Dollars: R$ ')
dollar = 5.28 # 1 dollar is worth 5.28 reais
dollarConvert = float(reais) / float(dollar)
print(f'Since $1.00 is {dollar} reais today, converting R${reais} into dollars, you will have: ${dollarConvert} dollars!')



"""06 - Conversion from Dollar currency to Real currency"""

print('Convert the Dollar currency into Real currency.')
dollar = ('Type how many Dollars you want to convert into Reais: $ ')
real = 0.19 #1 real is worth 0.19 dollars
realConvert = float(dollar) * float(real)
print(f'As R$1.00 real is{real} dollars today, converting ${dollar} into dollars, you will have: R${realConvert} reais!')