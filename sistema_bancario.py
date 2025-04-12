menu = """

[d] depositar
[s] sacar
[e] extrato
[q] sair

=> """

saldo = 0
LIMITE = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Valor a ser depositado: R$"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f} \n"
            print("Depósito realizado com sucesso.")
        else:
            print("Depósito não realizado: valor inválido. Tente novamente")

    elif opcao == "s":
        print("Saque")
        valor = float(input("Valor a ser sacado: R$"))
        if valor > saldo:
            print("Saque não realizado: saldo insuficiente para o saque")
        else:
            if valor > 0:
                if valor > LIMITE:
                    print("O valor máximo por saque é de R$500,00. Tente novamente")
                else:
                    num_saques += 1
                    if num_saques > LIMITE_SAQUES:
                        print("Saque não realizado: limite de saques diários atingidos")
                    else:
                        saldo -= valor
                        extrato += f"Saque de R$ {valor:.2f} \n"
                        print("Saque realizado com sucesso.")
            else:
                print("Saque não realizado: valor inválido. Tente novamente")

    elif opcao == "e":
        if not extrato:
            print("Não foram feitas transações até o momento.")
        else:
            print("----------Extrato----------")
            print(extrato)
            print("---------------------------")
        print(f"Saldo atual: R$ {saldo:.2f} \n")

    elif opcao == "q":
        break
    else:
        print("Operação inválida, selecione novamente a opção desejada")