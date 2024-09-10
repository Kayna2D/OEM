import math
from  decimal import Decimal

# Constantes
c = 3 * 10**8  # Velocidade da luz em m/s
epsilon_0 = 8.85 * 10**-12  # Permissividade do vácuo em F/m
Z_0 = 377  # Impedância do vácuo em ohms

def menu():
  while True:
    print("1 - Campo eletrico maximo (Em)")
    print("2 - Campo magnetico maximo (Bm)")
    print("3 - Intensidade")
    print()
    print("4 - Frequencia")
    print("5 - Comprimento")
    print("6 - Numero de ondas")
    print("7 - Frequencia angular")
    print("0- Sair\n")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
      em()
      print()
    elif opcao == 2:
      bm()
      print()
    elif opcao == 3:
      intensidade()
      print()
    elif opcao == 4:
      frequencia()
      print()
    elif opcao == 5:
      comprimento()
      print()
    elif opcao == 6:
      numeroOndas()
      print()
    elif opcao == 7:
      frequenciaAngular()
      print()
    elif opcao == 0:
      print("Saindo...")
      break

def em():
    print("Para obter Bm e I Entre com o campo elétrico máximo (Em) em V/m:")
    Em = float(input())
    
    Bm = Em / c
    I = 0.5 * epsilon_0 * c * Em**2
    
    print(f'Campo magnético máximo (Bm): {Decimal(Bm):.2E} T')
    print(f'Intensidade (I): {Decimal(I):.2E} W/m²')

def bm():
    print("Para obter Em e I entre com o campo magnético máximo (Bm) em T:")
    Bm = float(input())
    
    Em = c * Bm
    I = 0.5 * (Em**2 / Z_0)
    
    print(f'Campo elétrico máximo (Em): {Decimal(Em):.2E} V/m')
    print(f'Intensidade (I): {Decimal(I):.2E} W/m²')

def intensidade():
    print("Para obter Em e Bm Entre com a intensidade (I) em W/m²:")
    I = float(input())
    
    Em = math.sqrt((2 * I) / (epsilon_0 * c))
    Bm = Em / c
    
    print(f'Campo elétrico máximo (Em): {Decimal(Em):.2E} V/m')
    print(f'Campo magnético máximo (Bm): {Decimal(Bm):.2E} T')

#Funções 2
def frequencia():
  print("Entre com a frequencia (Hz)")
  f = float(input()) * 10**11

  l = c / f
  k = 2 * math.pi / l
  w = 2 * math.pi * f

  print('Comprimento (m): %.2E' % Decimal (l))
  print('Numero de ondas (rad/m): %.2E' % Decimal (k))
  print('Frequencia angular (rad/s): %.2E' % Decimal (w))


def comprimento():
  print("Entre com o comprimento (m): ")
  l = float(input()) * 10**-10

  f = c / l
  k = 2 * math.pi / l
  w = 2 * math.pi * f

  print('Frequencia (Hz): %.2E' % Decimal (f))
  print('Numero de ondas (rad/m): %.2E' % Decimal (k))
  print('Frequencia angular (rad/s): %.2E' % Decimal (w))

def numeroOndas():
  print("Entre com numero de ondas (rad/m): ")
  k = float(input()) * 10**-1

  l = 2 * math.pi / k
  f = c / l
  w = 2 * math.pi * f

  print('Frequencia (Hz): %.2E' % Decimal (f))
  print('Comprimento (m): %.2E' % Decimal (l))
  print('Frequencia angular (rad/s): %.2E' % Decimal (w))

def frequenciaAngular():
  print("Entre com a frequencia angular (rad/s): ")
  w = float(input()) * 10**6
  
  f = w / (2 * math.pi)
  l = c / f
  k = 2 * math.pi / l

  print('Comprimento (m): %.2E' % Decimal (l))
  print('Numero de ondas (rad/m): %.2E' % Decimal (k))
  print('Frequencia (Hz): %.2E' % Decimal (f))

c = 3 * 10**8

menu()
