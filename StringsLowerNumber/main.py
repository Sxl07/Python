x=input("digite un numero(n): ")
n=len(x)

k=int(input("digite un numero k (k < n): "))
while n<=k:
    print("El numero digitado es mayor que n(longitud de la cadean de texto, vuelve a digitarlo.)")
    k=int(input("digite un numero k (k < n): "))

result=""
xs=sorted(x,reverse=True)
primerCero = x.find("0")

if '0' in x and primerCero==k:
    nuevaCadena = x[:primerCero-k] + x[primerCero:]
    result=nuevaCadena

elif len(set(x)) == 1:
    result = x[:-k]

else:
    del xs[0:k]
    for j in x:
        if j in xs:
            result+=j

print("El numero mas pequeño encontrado es: ","{}".format(int(result)))