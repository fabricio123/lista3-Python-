maior = 0
c = 0 

while c <=5:
    n = int(input('Digite um numero: '. format(c))) 
    if n > maior: 
       maior = n 
    c = c+1
print('O maior numero é {}'.format( maior))

