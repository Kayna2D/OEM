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
      print()
      em()
      print()
    elif opcao == 2:
      print()
      bm()
      print()
    elif opcao == 3:
      print()
      intensidade()
      print()
    elif opcao == 4:
      print()
      frequencia()
      print()
    elif opcao == 5:
      print()
      comprimento()
      print()
    elif opcao == 6:
      print()
      numeroOndas()
      print()
    elif opcao == 7:
      print()
      frequenciaAngular()
      print()
    elif opcao == 0:
      print("Saindo...")
      break

def em():
    print("Entre com a amplitude do campo eletrico: ")
    Em = float(input())
    
    Bm = Em / c
    I = 0.5 * epsilon_0 * c * Em**2
    
    print(f'Campo magnético máximo: {Decimal(Bm):.2E} T')
    print(f'Intensidade: {Decimal(I):.2E} W/m²')

def bm():
    print("Entre com a amplitude do campo magnetico: ")
    Bm = float(input())
    
    Em = c * Bm
    I = 0.5 * (Em**2 / Z_0)
    
    print(f'Campo elétrico máximo: {Decimal(Em):.2E} V/m')
    print(f'Intensidade {Decimal(I):.2E} W/m²')

def intensidade():
    print("Entre com a intensidade: ")
    I = float(input())
    
    Em = math.sqrt((2 * I) / (epsilon_0 * c))
    Bm = Em / c
    
    print(f'Campo elétrico máximo: {Decimal(Em):.2E} V/m')
    print(f'Campo magnético máximo: {Decimal(Bm):.2E} T')

#Funções 2
def frequencia():
  print("Entre com a frequencia")
  f = float(input()) 

  l = c / f
  k = 2 * math.pi / l
  w = 2 * math.pi * f

  print('Comprimento: %.2E m' % Decimal (l))
  print('Numero de ondas: %.2E rad/m' % Decimal (k))
  print('Frequencia angular: %.2E rad/s' % Decimal (w))


def comprimento():
  print("Entre com o comprimento: ")
  l = float(input()) 

  f = c / l
  k = 2 * math.pi / l
  w = 2 * math.pi * f

  print('Frequencia: %.2E Hz' % Decimal (f))
  print('Numero de ondas: %.2E rad/m' % Decimal (k))
  print('Frequencia angular: %.2E rad/s' % Decimal (w))

def numeroOndas():
  print("Entre com numero de ondas: ")
  k = float(input())

  l = 2 * math.pi / k
  f = c / l
  w = 2 * math.pi * f

  print('Frequencia: %.2E Hz' % Decimal (f))
  print('Comprimento: %.2E m' % Decimal (l))
  print('Frequencia angular: %.2E rad/s' % Decimal (w))

def frequenciaAngular():
  print("Entre com a frequencia angular: ")
  w = float(input()) 
  
  f = w / (2 * math.pi)
  l = c / f
  k = 2 * math.pi / l

  print('Comprimento: %.2E m' % Decimal (l))
  print('Numero de ondas: %.2E rad/m' % Decimal (k))
  print('Frequencia: %.2E Hz' % Decimal (f))


print("Autores:")
print("Kayna de Deus Ferreira da Silva")
print("Mario Eugenio Silva")
print()
print("------------------------------------------------------------------------------------")
print()
print("Calculadora OEM")
print("Ondas eletromagneticas sao formadas pelos campos eletricos e magneticos e destacam-se por sua propagacao no vacuo")
print("O programa abaixo faz conversoes dos dados relevantes as ondas eletromagneticas")
print("Deve ser entrado um valor para que o programa o converta para seus dados relacionados:")
print("Relacoes 1: frequencia; comprimento; frequencia angular; numero de ondas")
print("Relacoes 2: amplitude do campo eletrico; amplitude do campo magnetico; intensidade")
print()
print("------------------------------------------------------------------------------------")
print()
menu()