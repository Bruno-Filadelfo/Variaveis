#Calculadora Simples
#num1 = int (input('Digite um numéro: '))
#operador = input('Digite o operador (+. -, *, /): ')
#num2 = int (input('Digite o segundo numéro: '))
#if operador == '+':
#    resultado = num1 + num2
#elif operador == '-':
#    resultado = num1 - num2
#elif operador == '*':
#    resultado = num1 * num2
#elif operador == '/':
#    resultado = num1 / num2
#    if num2 != 0:
#        resultado = num1 / num2
#    else:
#        resultado = 'Erro: Divisão por zero'
#else:
#    resultado = 'Operador inválido'
#print('resultado:',resultado)  

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite mais um numero: '))
multiplicação = n1 * n2
adição = n1 + n2 
divisão = n1 / n2 
subtração = n1 - n2
print('O resultado final da soma é',multiplicação,adição,divisão,subtração)