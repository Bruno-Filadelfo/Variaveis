texto = 'Bruno'
for letra in texto:
    print(letra)

for numero in range(0 , 15):
    print(numero)  

##################################
lista = [1, 2, 3, 4, 5]
for item in lista:
    print(item)

#################################

for i in range(5):
    print(i)

##################################

lista = ['a', 'b', 'c', 'd']
for indice, elemento in enumerate(lista):
    print(f'Índice: {indice}, Elemento: {elemento}')

#####################################

dicionario = {'a': 1, 'b': 2, 'c': 3}
for chave, valor in dicionario.items():
    print(f'Chave: {chave}, Valor: {valor}')

#############################################
texto = 8 , 10 , 15 , 22 , 65 
print(len(texto))
print(min(texto))
print(max(texto))
print(sum(texto))


#############################################
for carro in range(2, 5, 8):
    print(carro)

##############################################    

numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)

############################
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)    


texto = "Desenvolvedor Python"
nova_string = ''
for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)            


for n in range(0, 50, 60):
    print(n) 
if n > 50:
    print('o valor é o dobro')
else:
    print('o valor 50 é menor')       


for numero in range(20, 10, -2):
    print(numero)     
    







    