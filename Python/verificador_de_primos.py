#Pedimos um numero ao usuario!
a = int(input("Informe um numero:\n"))

#Colocamos uma variavel inicializada com 0 para ser contador!
div = 0
#faremos um laço for para verificar se é primo ou não!
for x in range(1, a+1):
    resto = a % x
    if resto == 0:
        div +=1

if div == 2:
    print(f"numero {a} é primo!")
else :
    print(f"numero {a} não é primo!")
