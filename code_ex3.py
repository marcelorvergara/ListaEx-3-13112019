#code_ex3.py
#import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
def teste():
  i = 0
  x = 10000
  while (x>i):
    print("/", end="\r", flush=True)
    print("", end="\r", flush=True)
    print("-", end="\r", flush=True)
    print("", end="\r", flush=True)
    print("|", end="\r", flush=True)
    print("", end="\r", flush=True)
    print("-", end="\r", flush=True)
    print("", end="\r", flush=True)
    print("\\", end="\r", flush=True)
    print("", end="\r", flush=True)
    i = i +1

def de_1a_100():
  i = 1
  tot = 0
  for i in range(1,101):
    tot = tot + i
  print (tot)

def seq_20_num():
  x = int(input("Digite um número: "))
  maior = x
  menor = x
  soma = 0
  cont = 0
  for i in range(20):
    cont = cont +1
    x = int(input("Digite um número: "))
    if x > maior:
      maior = x
    if x < menor:
      menor = x
    soma = soma + x
  print("O menor número é o: ", menor)
  print("O maior número é o: ", maior)
  print("A média é: ", soma/cont)
  print("A soma é: ", soma)
  print("Quantidade de números digitados é: ", cont)
  sleep(5)
  clear()

def seq_n_num():
  soma = 0
  tot = 0
  n = None
  n = int(input("Digite um número ou digite 0 para sair: "))
  maior = n
  menor = n
  while n != 0:
    tot = tot +1
    soma = soma + n
    if n > maior:
      maior = n
    if n < menor:
      menor = n
    n = int(input("Digite um número ou digite 0 para sair: "))

  print("O menor número é o: ", menor)
  print("O maior número é o: ", maior)
  print("A média é: ", soma/tot)
  print("A soma é: ", soma)
  print("Quantidade de números digitados é: ", tot)
  sleep(5)
  clear()

def seq_0():
  cont = 0
  soma = 0
  maior = 0
  menor = 0
  while True:
    x = int(input(f"Digite um número inteiro: "))
    soma = soma + x
    if cont == 0:
      maior = x
      menor = x
    if x != 0:
      cont = cont + 1
    if x >= maior:
      maior = x
    if x <= menor:
      menor = x
    elif x == 0:
     print ("A Soma é: ", soma)
     print ("Numeros digitados: ", cont)
     print("A media é: ", soma/cont)
     print ("O maior numero é: ", maior)
     print("O menor é: ", menor)
     print("Fim do programa!")
     break 
    sleep(5)
    clear()

def num_pri():
  menor = int(input("Digite o menor numero: "))
  maior = int(input("Digite o maior numero: "))
  cont = 0
  primos = 0
 
  for divisor in range (menor, maior,1):
    divisores = 0
    i = 2
    while i < divisor:
      if divisor % i == 0:
        i = i +1
        divisores = divisores + 1
        if divisores > 1:
          break
      else:
        i = i + 1
    if divisores <= 1:
      print (divisor)
      primos = primos + 1
  print("O total de números primos encontrados foi: ", primos)
  sleep(5)
  clear()

def tabuada():
  x = 1
  y = 1

  for x in range (11):
    for y in range (11):
      print (f"A soma de {x} + {y} é: ", x+y )

  sleep(20)
  clear()

def fibo():
  primeiro = 0
  segundo = 1
  final = int(input("Digite a quantidade de números a apresentar: "))
  print(primeiro)
  print(segundo)
  for x in range (final):
    soma = primeiro + segundo
    print (soma)
    primeiro = segundo
    segundo = soma
  sleep(10)
  clear()

def prog_arit():
  pri = int(input("Digite o primeiro numero: "))
  seg = int(input("Digite o segundo numero: "))
  final = int(input("Digite o último número da sequencia a ser apresnetada: "))

  const = seg-pri

  for n in range(pri,final, const):
    print(n)
  
  print("FIM da Sequência")
  
  sleep(10)
  clear()

def primsn():
  num = int(input("Digite um numero: "))
  divisores = 0
  for divisor in range (1, num):
   if num % divisor == 0:
     divisores = divisores + 1
     if divisores > 1:
      break
  if divisores > 1:
    print ("Não é primo")
  else:
    print(num, "é um número primo")
  teste()
  sleep (5)
  clear()

def prim2():
  num=1
  while num != 0:
    num = int(input("Digite um numero para validar se é primo ou 0 para sair: "))
    divisores = 0
    for divisor in range (1, num):
      if num % divisor == 0:
        divisores = divisores + 1
        if divisores > 1:
          break
    if divisores > 1:
      print ("Não é primo")
    else:
      print(num, "é um número primo")
  else:
    print ("Inté!")

  sleep (5)
  clear()

def fatorial():
  num = int(input("Digite um numero: "))
  tot = 1
  if num == 0:
    print(f"O fatorial de {num} é 1")
  elif num == 1:
    print(f"O fatorial de {num} é 1")
  else:
    for i in range (1,num):
      tot = (tot * (i+1))
  print(f"O fatorial de {num} é {tot}")

  sleep(5)
  clear()

def proj_e():
  i = 0
  sum = 0
  while (i < 999):
    i = i + 1
    if (i % 3 == 0) and (i % 15 == 0):
      sum = sum + i
    else:
      if (i % 3 == 0):
        sum = sum + i
    
      else:
        if (i % 5 == 0):
          sum = sum + i
  teste()
  sleep (3)
  print (sum)
  sleep (4)
  clear()


  