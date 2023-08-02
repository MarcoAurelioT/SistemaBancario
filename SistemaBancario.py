menu = """
======== MENU ========
    [S] SACAR
    [D] DEPOSITO
    [E] EXTRATO
    [Q] SAIR
======================
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "s":
          valor = float(input("Informe o valor so saque: "))

          excedeu_saldo = valor > saldo

          excedeu_limite = valor > limite

          excedeu_saques = numero_saques >= LIMITE_SAQUES

          if excedeu_saldo :
              print("Operação falhou! Você não tem saldo suficiente.")

          elif excedeu_limite:
              print("Operação falhou! O valor do saque excede o limite.")

          elif excedeu_saques:
              print("Operação falhou! Número máximo de saques excedido.")

          elif valor > 0:
            saldo += valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1   

          else:
              print("Operação falhou! O valor informado é invalido")           
    elif opcao == "d":
       
        valor=float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("A operação falhou! O valor informado é invalido.")    

    elif opcao == "e":
        print("EXTRATO")

    elif opcao == "q":
        print("SAIR")

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
