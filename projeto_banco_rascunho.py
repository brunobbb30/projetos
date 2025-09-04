#Rascunho do projeto

# Operações: sacar, depositar, extrato (contendo saldo, sacado, e depositado)
# limite de 3 saques de 500 reais por dia


saldo = 0.0
qtd_de_saques = 0
deposito_acumulado = 0.0
saque_acumulado = 0.0
LIMITE_SAQUES = 3
LIMITE_VALOR = 500.0
menu = (f"""{" MENU ".center(30,"-")}
      
    Tecle [d] para depositar
      
    Tecle [s] para sacar
      
    Tecle [e] para extrato
    
    Tecle [q] para sair
        
""")

while True:
    
    opcao = input(menu)
    if opcao == "d":
        valor_deposito = float(input("Digite o valor a ser depositado: R$ "))
        saldo += valor_deposito
        deposito_acumulado += valor_deposito
        print("**Valor depositado com sucesso!**\n")
    elif opcao == "s":
        if qtd_de_saques >= LIMITE_SAQUES:
            print("\nAVISO: Quantidade de saques excedida. Tente novamente amanhã.\n")
            continue
        valor_saque = float(input("Digite o valor a ser sacado: R$ "))
        if valor_saque > LIMITE_VALOR:
            print("\nAVISO: O limite de saque é de R$ 500,00.\n")
            valor_saque = float(input("Digite o valor a ser sacado: R$ "))
        elif valor_saque > saldo:
            print(f"\nAVISO: Saldo insuficiente. Seu saldo é de R${saldo:.2f}\n")
            continue
        saldo -= valor_saque
        qtd_de_saques += 1
        saque_acumulado += valor_saque
        print("**Valor sacado com sucesso!**\n")
    elif opcao == "e":
        print(f"Depositado: {deposito_acumulado:.2f}\nSacado: {saque_acumulado:.2f}\nSaldo: {saldo:.2f}\n")
    elif opcao == "q":
        break
            