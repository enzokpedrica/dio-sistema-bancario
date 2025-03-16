quantidade_saque = 0
saldo = []

while True:
    print("=============================")
    print("Bem vindo ao Sistema Bancario")
    print("=============================\n")

    resposta = int(input("O que deseja fazer?\n 1 - Sacar\n 2 - Depositar\n 3 - Consultar Extrato\n 4 - Saldo Atual\nSelecione a opção: "))

    print(" ")

    if resposta	== 1:
        if quantidade_saque <= 3:
            saque = float(input("Qual o valor do saque?\n"))
            saque = saque *-1
            saldo.append(saque)
            quantidade_saque += 1
        else:
            print("=== Quantidade de Saques excedida! ===\n")

    elif resposta == 2:
        deposito = float(input("Qual o valor do depósito?\n"))
        if deposito > 0:
            saldo.append(deposito)
        else:
            print("Favor depositar somente valores positovs!!!\n")
            
    
    elif resposta == 3:
        print(f"Extrato Detalhado: {saldo}\n")

    elif resposta == 4:
        print(f"Seu saldo atual é R$ {sum(saldo):.2f}\n")
    
    else:
        print("Obrigado, até mais\n")








