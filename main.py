quantidade_saque = 0
saldo = []
usuarios = {}


def saque():
    global quantidade_saque
    if quantidade_saque <= 3:
            saque = float(input("Qual o valor do saque?\n"))
            saque = saque *-1
            saldo.append(saque)
            quantidade_saque += 1
    else:
        print("=== Quantidade de Saques excedida! ===\n")

def depositar():
    deposito = float(input("Qual o valor do depósito?\n"))
    if deposito > 0:
        saldo.append(deposito)
    else:
        print("Favor depositar somente valores positivos!!!\n")

def extrato():
    print(f"Extrato Detalhado:")
    for i in saldo:
        print(f"R$ {i:.2f}")

def saldo_conta():
    print(f"Seu saldo atual é R$ {sum(saldo):.2f}\n")

def criar_usuario(nome,conta):
    if nome in usuarios:
        print("Esse nome já existe!!!")
    else:
        usuarios[nome] = conta
        print("Usuário Cadastrado")     


while True:
    print("=============================")
    print("Bem vindo ao Sistema Bancario")
    print("=============================\n")

    resposta = int(input("O que deseja fazer?\n 1 - Sacar\n 2 - Depositar\n 3 - Consultar Extrato\n 4 - Saldo Atual\n 5- Criar Conta\n Selecione a opção: "))
    print(" ")

    if resposta	== 1:
        saque()
    elif resposta == 2:
        depositar()
    elif resposta == 3:
        extrato()
    elif resposta == 4:
        saldo_conta()

    elif resposta == 5:
        nome = input("Digite seu Nome Completo: ")
        conta_int = int(input("Digite 4 Dígitos para sua Conta: "))
        conta_str = len(str(conta_int))
        
        if conta_str == 4:
            criar_usuario(nome, conta_int)
        else:
            print("Conta Inválida!!!")

    else:
        print("Obrigado, até mais\n")
        break
