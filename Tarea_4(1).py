#Tarea 4
#Computación Aplicada
#Alvarado Reyes, Ignacio               |A01656149
#Rangel García, Frida Berenice         |A01651385
#Villicaña Ibargüengoytia, José Rubén  |A01654347

import math

def f(x):
  f = math.exp(x**2)
  #f = 1 + ((math.exp(-x))*(math.sin(4*x)))
  #f = math.sin(math.pi*x)
  #f = 1 + ((math.exp(-x))*(math.cos(4*x)))
  #f = math.sin(math.sqrt(x))
  return f

def simpson3_8_Compuesto(a,b,n):
  h = (b-a)/n
  S = f(a) + f(b)              #Obtenemos los terminos inicial y final
  S_2 = 0                      #Grupo de elementos que se mutiplicaran por 2
  S_3 = 0                      #Grupo de elementos que se mutiplicaran por 3

  for i in range (1,n):
    k = a + i*h                #Calcular los saltos
    if i%3 == 0:               #Si es multiplo de 3 ese termino se tiene que multiplicar por 2
      S_2 = S_2 + f(k)
    else:                      #Si no es multiplo de 3 ese termino se tiene que multiplicar por 3
      S_3 = S_3 + f(k)

  S = S + (2*S_2) + (3*S_3)    #Suma de terminos
  S = (3*h/8)*S                #Multiplicación de termino inicial
  
  return S 

def main():
  a = float(input("Límite inferior de integración (a): "))
  b = float(input("Límite inferior de integración (b): "))
  n = int(input("Número de intervalos de integración (n) [Múltiplo de 3]: "))

  key = 0
  while key == 0:                       #Este método solo funciona con n siendo multiplos de 3.
    if n%3 == 0 and n>0:                #Si la condicion se cumple, n es multiplo de 3 y postivio
      key = 1
    else:
      n = int(input("Número de intervalos de integración (n) [Múltiplo de 3]: "))
  
  S = simpson3_8_Compuesto(a,b,n)
  print("Integración Simpson 3/4 Compuesto:  " ,(S))
  
main()