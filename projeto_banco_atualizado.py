# Operações:
#   Depositar
#       Somente valores positivos
#   Sacar
#       Limite de 3 saques por dia
#       Somente valores positivos
#       Limite de 500 reais por saque
#       Mensagem caso a conta não tenha saldo
#   Extrato
#       Listar todos os depósitos e saques realizados
#       Exibir o saldo atual da conta
#       Valores com formato R$ xxx.xx


saldo = 0.0
qtd_de_saques = 0
deposito_acumulado = 0.0
saque_acumulado = 0.0
extrato = "     EXTRATO     ".center(30,"-") + "\n\n"
LIMITE_SAQUES = 3
LIMITE_VALOR = 500.0
menu = (f"""\n{" MENU ".center(30,"=")}
      
    Tecle [d] para depositar
      
    Tecle [s] para sacar
      
    Tecle [e] para extrato
    
    Tecle [q] para sair
        
""")

while True:
    
    opcao = input(menu)
    if opcao == "d":
        valor_deposito = float(input("\nDigite o valor a ser depositado: R$ "))
        while valor_deposito < 0:
            print("\nAVISO: Operação inválida. O valor deve ser positivo.\n")
            valor_deposito = float(input("Digite o valor a ser depositado: R$ "))
        print(f"\nDespositar R$ {valor_deposito:.2f}.")
        confirmacao_deposito = input("[c]Confirmar\n[m] Retornar ao menu\n")
        while confirmacao_deposito != "c" and confirmacao_deposito != "m":
            print("\nValor inválido.")
            print(f"\nDespositar R$ {valor_deposito:.2f}.")
            confirmacao_deposito = input("[c]Confirmar\n[m] Retornar ao menu\n")
        if confirmacao_deposito == "c":
            saldo += valor_deposito
            deposito_acumulado += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print("\n**Valor depositado com sucesso!**")
        else:
            continue
    elif opcao == "s":
        if qtd_de_saques >= LIMITE_SAQUES:
            print("\nAVISO: Quantidade de saques excedida. Tente novamente amanhã.")
            continue
        valor_saque = float(input("\nDigite o valor a ser sacado: R$ "))
        while valor_saque < 0:
            print("\nAVISO: Operação inválida. O valor deve ser positivo.")
            valor_saque = float(input("\nDigite o valor a ser sacado: R$ "))
        while valor_saque > LIMITE_VALOR:
            print("\nAVISO: O limite de saque é de R$ 500,00.")
            valor_saque = float(input("\nDigite o valor a ser sacado: R$ "))
        if valor_saque > saldo:
            print(f"\nAVISO: Saldo insuficiente. Seu saldo é de R${saldo:.2f}")
            continue
        print(f"\nSacar R$ {valor_saque:.2f}.")
        confirmacao_saque = input("[c]Confirmar\n[m] Retornar ao menu\n")
        while confirmacao_saque != "c" and confirmacao_saque != "m":
            print("\nValor inválido.")
            print(f"\nSacar R$ {valor_saque:.2f}.")
            confirmacao_saque = input("[c]Confirmar\n[m] Retornar ao menu\n")
        if confirmacao_saque == "c":
            saldo -= valor_saque
            qtd_de_saques += 1
            saque_acumulado += valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            print("\n**Valor sacado com sucesso!**")
        else:
            continue
    elif opcao == "e":
        pausa = "a"
        while pausa != "m":
            print("\n"+extrato)
            print(f"Total de depósitos: R$ {deposito_acumulado:.2f}\nTotal de saques: R$ {saque_acumulado:.2f}\nSaldo: R$ {saldo:.2f}")
            pausa = input("-".center(30,"-") + "\n\n""Tecle [m] para Menu\n")
    elif opcao == "q":
        break
    else:
        print("\nOpção Inválida")
            