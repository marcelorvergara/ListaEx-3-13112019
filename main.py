#main.py

import sys
from code_ex3 import *

i = 0
while 1>i :
  
  print ("Lista de Ex. 3 - Escolha uma opção: ")
  print("\t")
  print("Opçao 1 - soma de 1 a 100")
  print("Opçao 2 - sequência de 20 numeros")
  print("Opçao 3 - sequência de n números")
  print("Opçao 4 - sequência de n números novamente")
  print("Opçao 5 - numeros primos")
  print("Opçao 6 - tabuada")
  print("Opçao 7 - sequência de Fibonacci")
  print("Opçao 8 - progressão aritmética")
  print("Opçao 9 - validar se um número é primo")
  print("Opçao 10 - é primo?")
  print("Opçao 11 - fatorial")
  print("Opçao 12 - project Euler")
  print("Opçao 13 - SAIR")
  
  opcao = input(f"Digite aqui: ")

  if opcao.isdigit() == False:
    opcao = 15

  opcao = int(opcao)
  if opcao <= 14: 
    if opcao == 13:
      i=2
      print("Inté!")
    if opcao == 1:
      de_1a_100()
      print("\t")

    if opcao == 2:
      seq_20_num()
      print("\t")

    if opcao == 3:
      seq_n_num()
      print("\t")

    if opcao == 4:
      seq_n_num()
      print("\t")

    if opcao == 5:
      num_pri()
      print("\t")
    
    if opcao == 6:
      tabuada()
      print("\t")

    if opcao == 7:
      fibo()
      print("\t")
    
    if opcao == 8:
      prog_arit()
      print("\t")
    
    if opcao == 9:
      primsn()
      print("\t")
    
    if opcao == 10:
      prim2()
      print("\t")

    if opcao == 11:
      fatorial()
      print("\t")
    
    if opcao == 12:
      proj_e()
      print("\t")

  else:
    print("  ")
    print("***Comando inválido. Digite valores de 1 a 12 ou 13 para sair***")
    teste()
    sleep(5)
    clear()
