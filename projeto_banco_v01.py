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

    #Depósito
    if opcao == "d":

        valor_deposito = float(input("\nDigite o valor a ser depositado: R$ "))

        #Conferência e requisição de um valor positivo
        while valor_deposito < 0:
            print("\nAVISO: Operação inválida. O valor deve ser positivo.\n")
            valor_deposito = float(input("Digite o valor a ser depositado: R$ "))

        #Confirmação da operação
        print(f"\nDespositar R$ {valor_deposito:.2f}.")
        confirmacao_deposito = input("[c]Confirmar\n[m] Retornar ao menu\n")

        #Conferência e requisição de uma opção válida
        while confirmacao_deposito != "c" and confirmacao_deposito != "m":
            print("\nValor inválido.")
            #Confirmação da operação
            print(f"\nDespositar R$ {valor_deposito:.2f}.")
            confirmacao_deposito = input("[c]Confirmar\n[m] Retornar ao menu\n")

        #Em caso de operação confirmada
        if confirmacao_deposito == "c":
            saldo += valor_deposito
            deposito_acumulado += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print("\n**Valor depositado com sucesso!**")

        #Em caso de operação abortada
        else:
            continue
    
    #Saque
    elif opcao == "s":

        #Verificação de limite diário de saques
        if qtd_de_saques >= LIMITE_SAQUES:
            print("\nAVISO: Quantidade de saques excedida. Tente novamente amanhã.")
            continue

        valor_saque = float(input("\nDigite o valor a ser sacado: R$ "))

        #Conferência e requisição de um valor positivo 
        while valor_saque < 0:
            print("\nAVISO: Operação inválida. O valor deve ser positivo.")
            valor_saque = float(input("\nDigite o valor a ser sacado: R$ "))

        #Conferência de limite de valor por saque
        while valor_saque > LIMITE_VALOR:
            print("\nAVISO: O limite de saque é de R$ 500,00.")
            valor_saque = float(input("\nDigite o valor a ser sacado: R$ "))

        #Verifica se há saldo na conta
        if valor_saque > saldo:
            print(f"\nAVISO: Saldo insuficiente. Seu saldo é de R${saldo:.2f}")
            continue

        #Confirmação da operação
        print(f"\nSacar R$ {valor_saque:.2f}.")
        confirmacao_saque = input("[c]Confirmar\n[m] Retornar ao menu\n")

        #Conferência e requisição de uma opção válida
        while confirmacao_saque != "c" and confirmacao_saque != "m":
            print("\nValor inválido.")
            #Confirmar operação
            print(f"\nSacar R$ {valor_saque:.2f}.")
            confirmacao_saque = input("[c]Confirmar\n[m] Retornar ao menu\n")

        #Em caso de operação confirmada
        if confirmacao_saque == "c":
            saldo -= valor_saque
            qtd_de_saques += 1
            saque_acumulado += valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            print("\n**Valor sacado com sucesso!**")

        #Em caso de operação abortada
        else:
            continue
    
    #Extrato
    elif opcao == "e":

        #Variável apenas para fins de pausa de fluxo
        pausa = "a"

        while pausa != "m":
            print("\n"+extrato)
            print(f"Total de depósitos: R$ {deposito_acumulado:.2f}\nTotal de saques: R$ {saque_acumulado:.2f}\nSaldo: R$ {saldo:.2f}")
            pausa = input("-".center(30,"-") + "\n\n""Tecle [m] para Menu\n")

    #Fechar programa
    elif opcao == "q":
        break
    
    #Em caso de opção inválida
    else:

        print("\nOpção Inválida")
            