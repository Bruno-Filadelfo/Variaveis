a = 2
b = 2
c = 3
resultado = a == b and c < b 
print(resultado)

a = 15 
b = 20 
c = 30
d = 35
resultado = a > d 
print(resultado)
print (type(resultado))

a = 10 
b = 10
c = 30
resultado = a == b and 30 > 10
print(resultado)

a = 100
b = 200
c = 300
resultado = a == b  or 300 > 500
print(resultado)


a = 1000
b = 2000

if not 2000 < 1000:
    print("B é maior que A")
else:
    print("A é maior que B")    


a = 30 
b = 60

if 30 < 60:
    print("A é maior que B")
else:
    print("B é maior que A")    