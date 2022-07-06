
n1=int(input("Insira um número :"))
n2=int(input("Insira outro número :"))
operacao=int(input("Insira 1 para somar, 2 para subtrair, 3 para multiplicar e 4 para dividir : "))

if(operacao==1):
    {
       print("resultado =",n1+n2)
    }
elif(operacao==2):
    {
        print("resultado =",n1-n2)
    }

elif(operacao==3):
    {
        print("resultado =",n1*n2)
    }

elif(operacao==4):
    {
        print("resultado =",n1/n2)
    }
else:
    {
        print("Número da operação inserido incorretamente")
    }