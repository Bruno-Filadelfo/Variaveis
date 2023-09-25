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

#n1 = int(input('Digite um numero: '))
#n2 = int(input('Digite mais um numero: '))
#multiplicação = n1 * n2
#adição = n1 + n2 
#divisão = n1 / n2 
#subtração = n1 - n2
#print('O resultado final da soma é',multiplicação,adição,divisão,subtração)

####################################################

# Solicita ao usuário para inserir três números
#num1 = float(input("Digite o primeiro número: "))
#num2 = float(input("Digite o segundo número: "))
#num3 = float(input("Digite o terceiro número: "))

# Calcula a média dos três números
#media = (num1 + num2 + num3) 

# Exibe a média
#print(f"A média dos números {num1}, {num2} e {num3} é {media}.")

#cores = 'azul, amarelo, verde'
#print(type(cores))
########################################################
horário = 'tarde'

if horário == 'manhã':
    print('Bom dia!')
elif horário == 'tarde!':
    print('Boa tarde!')
else:
    print('Boa noite!')            
########################################################
#frutas = ['maça', 'uva', 'laranja']
#for frutas in frutas:
#    print(frutas)

intervalo = range(10)
print([])

for numero in range(10): # Range é responsável para definir um intervalo
  dobro = numero * 2
  print("O dobro de", numero, "é", dobro)
