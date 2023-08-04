def fibonacci(valor):
  if valor==0 or valor==1:
    return valor
  return (fibonacci(valor-1)+fibonacci(valor-2))
mes=int(input("digita el numero de mes para la cantidad de parejas de conejos "))
print(fibonacci(mes))
