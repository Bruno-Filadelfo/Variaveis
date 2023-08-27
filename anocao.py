nome = "Bruno"
sobrenome = "Carvalho Filadelfo"
idade = 25
altura = 1.80
verdadeiro = True
profissao = "Desenvolvedor Python"
print('Nome Completo:', nome, sobrenome)
print('Idade:', idade)
print('Profissão:', profissao)
print('Altura:', altura)
print('Confirma essa Altura ?', True)

empresas_de_carro = "Toyota, Fiat, Chevrole"
modelos = "Corola, Touro, Cruze"
print(empresas_de_carro)
print(modelos)

idade = 27
altura = 1.88
numero = 15
print (type(idade))
print(type(altura))
print(type(numero))

largura = float(input("Digite a Largura do Retângulo: "))
altura = float(input("Digite a Altura do Retângulo: "))
area = largura * altura
print("Á area do Retângulo é:", area)

#########################################

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
anos_faltantes = 100 - idade
ano_atual = 2023 
ano_100_anos = ano_atual + anos_faltantes
print(f"Olá, {nome}! Você terá 100 anos em {ano_100_anos}.")

##########################################

matemática = int(input("Nota final de Matemática foi: "))
Português = int(input("Nota final de Portguês foi: "))
História = int(input("Nota final de História foi: "))

nota = matemática, Português, História
print(f"A, {nota}! a nota final foi")

nota1 = float(input("Digite a primeira nota: ")) 
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print("A média das notas é:", media)

numero = int(input("Digite um número inteiro: "))
dobro = numero * 2
print(f"O dobro de {numero} é {dobro}.")

#ENTRADA DE DADOS 

nome = input("Qual é o seu nome? ")
idade = int(input("Quantos anos você tem ? "))
altura = float(input("Qual é a sua altura? "))
nascimento = input("Nascimento? ")
print(f"{nome} tem {idade} anos e {altura} de altura e nascido {nascimento}")

numero1 = int(input("Digite um numero: "))
numero2 = input("Digite outro numero: ")
numero2 = int(numero2)
print(numero1 / numero2)

if False:
    print("Verdadeiro")
elif False:
    print("é falço")
else: 
    print("Não é verdadeiro")

if False:
    print("Meu Carro é falço")
print("Meu Carro é Verdadeiro")

if True:
    print("meu carro é verdadeiro")
else:
    print("Meu carro é falço")

if False:
    print("meu carro é verdadeiro")  
else:
    print("meu carro é falço")  

if False:
    print("Verdadeiro")
else:
    print("falso") 

##############################################

if True:
    print("Carro Falso")
else:
    print("Carro Verdadeiro") 

##############################################

if False:
    print("É merda de verdade")   
else:
    print("não é merda")
if False:
    print("É merda de verdade")
else:
    print("não é merda") 

if False:
    print("meu carro é vermelho")
else:
    print("meu carro não é vermelho")

if False:
    print("Carro verde")
elif True:
    print("Agora viro vermelho")
else:
    print("verdadeiro")        

empresas_de_carros = "volkswagen, chevrolet, hyundai"
modelo_dos_carros = "Nivus, Camaro, hb20"
cores_dos_carros = "Amarelo , Vermelho, Azul"
ano_dos_carros = "2016, 2018, 2020"
print(f"As Empresas {empresas_de_carros}") 
print(f"nos modelos {modelo_dos_carros}") 
print(f"com os carros {cores_dos_carros}")
print(f"no ano de {ano_dos_carros}")

if False:
    print("Todos Carros são verdadeiro")
elif True:
    print("1 carro é falso")    
else:
    print("nenhum dos carros são verdadeiros")    

if True:
    print("Todos carros são verdadeiro")
elif False:
    print("1 carro é falso")    
else:
    print("nenhum dos carros são verdadeiros ")    

nome = input("Qual é seu nome ?: ")
idade = int (input("Qual é a sua idade ?: "))
altura = float(input("Qual é a sua altura?: "))
print(f"Você se chama {nome}")
print(f"Você tem {idade} anos")
print(f"Sua altura é {altura}")

#Operadores Relacionais
#1
num1 = 5
num2 = 3
expressao = num1 > num2 #sinal maior
print(expressao)
#2
num1 = 5
num2 = 3
expressao = num1 < num2 #sinal menor
print(expressao)
#3
num1 = 5
num2 = 5 
expressao = num1 >= num2 #sinal maior ou igual
print(expressao)
#4
num1 = 4
num2 = 6
expressao = num1 <= num2 #sinal menor ou igual 
#5
nome1 = "Bruno"
nome2 = "Bruno"
nomes = nome1 != nome2  
print(nomes)