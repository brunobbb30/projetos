#Operações:
#   Geral
#       Limite de 10 transações por dia
#       Mensagem caso já tiver chegado ao limite de transações
#       OK Inserir as operações de depósito, saque e extrato em funções
#           OK Depósito: Função recebe argumentos apenas por posição
#           OK Saque: Função recebe argumentos apenas por nome
#           OK Extrato: Função recebe argumentos por posição (saldo) e por nome (extrato)
#       (+)Inserir funções de cadastro de usuários e cadastro de conta bancária (vincular com usuário)
#           (+)Usuário:
#               (+)armazenar em lista
#               (+)composto por: nome, data de nascimento, cpf, endereço
#                    (+)o endereço é uma string com o formato: logradouro, número - bairro - cidade/siglaEstado
#                    (+)cpf é somente números
#               (+)não se pode cadastras 2 usuários com o mesmo cpf
#           (+)Conta:
#               (+)armazenar em lista
#               (+)composto por: agência, número da conta, usuário
#               (+)o número da conta é sequencial, iniciando em 1
#               (+)o número da agência é fixo: 0001
#               (+)o usuário pode ter mais de uma conta, mas uma conta pertence apenas a um usuário
#   Depositar
#       Somente valores positivos
#   Sacar
#       Somente valores positivos
#       Limite de 500 reais por saque
#       Mensagem caso a conta não tenha saldo
#   Extrato
#       Listar todos os depósitos e saques realizados
#       Exibir data e hora de cada operação
#       Exibir o saldo atual da conta
#       Valores com formato R$ xxx.xx

from datetime import datetime, date

saldo = 0.0
qtd_de_saques = 0
deposito_acumulado = 0.0
saque_acumulado = 0.0
contador = 0
dia_da_ultima_operacao = date.today()
extrato = "     EXTRATO     ".center(30,"-") + "\n"
LIMITE_OPERACOES = 2
LIMITE_VALOR = 500.0
menu = (f"""\n{" MENU ".center(30,"=")}
      
    Tecle [d] para depositar
      
    Tecle [s] para sacar
      
    Tecle [e] para extrato
    
    Tecle [q] para sair
        
""")

def deposito (contador, dia_da_ultima_operacao, saldo, deposito_acumulado, extrato, LIMITE_OPERACOES):

    #Verifica limite de operações
    dia_da_verificacao = date.today()

    if dia_da_verificacao == dia_da_ultima_operacao:
        if contador >= LIMITE_OPERACOES:
            print("\nAVISO: Quantidade máxima de operações diárias atingida. Tente novamente amanhã.")

            #Variável apenas para fins de pausa de fluxo
            pausa = "a"
            while pausa != "m" and pausa != "q":
                pausa = input("Tecle [m] para Menu\nTecle [q] para Encerrar Sessão\n")
            
            if pausa == "m":
                return ("menu",)
            else:
                return ("encerrar",)
    else:
        contador = 0

    valor_deposito = float(input("\nDigite o valor a ser depositado: R$ "))

    #Conferência e requisição de um valor positivo
    while valor_deposito < 0:
        print("\nAVISO: Operação inválida. O valor deve ser positivo.\n")
        valor_deposito = float(input("Digite o valor a ser depositado: R$ "))

    #Confirmação da operação
    print(f"\nDespositar R$ {valor_deposito:.2f}.")
    confirmacao_deposito = input("[c] Confirmar\n[a] Abortar\n")

    #Conferência e requisição de uma opção válida
    while confirmacao_deposito != "c" and confirmacao_deposito != "a":
        print("\nValor inválido.")
        #Confirmação da operação
        print(f"\nDespositar R$ {valor_deposito:.2f}.")
        confirmacao_deposito = input("[c] Confirmar\n[a] Abortar\n")

    #Em caso de operação confirmada
    if confirmacao_deposito == "c":
        contador += 1
        dia_da_ultima_operacao = date.today()
        saldo += valor_deposito
        deposito_acumulado += valor_deposito
        data = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        extrato += f"\n{data}\nDepósito: R$ {valor_deposito:.2f}\n"
        print("\n**Valor depositado com sucesso!**")
        return "menu", contador, dia_da_ultima_operacao, saldo, deposito_acumulado, extrato

    #Em caso de operação abortada
    else:
        print("\nXX Operação abortada XX")
        return ("menu",)

def saque (*, contador, dia_da_ultima_operacao, saldo, saque_acumulado, extrato, LIMITE_OPERACOES, LIMITE_VALOR):
    #Verifica limite de operações
    dia_da_verificacao = date.today()

    if dia_da_verificacao == dia_da_ultima_operacao:
        if contador >= LIMITE_OPERACOES:
            print("\nAVISO: Quantidade máxima de operações diárias atingida. Tente novamente amanhã.")

            #Variável apenas para fins de pausa de fluxo
            pausa = "a"
            while pausa != "m" and pausa != "q":
                pausa = input("Tecle [m] para Menu\nTecle [q] para Encerrar Sessão\n")
            
            if pausa == "m":
                return ("menu",)

            else:
                return ("encerrar",)

    else:
        contador = 0

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
        return ("menu",)

    #Confirmação da operação
    print(f"\nSacar R$ {valor_saque:.2f}.")
    confirmacao_saque = input("[c] Confirmar\n[a] Abortar\n")

    #Conferência e requisição de uma opção válida
    while confirmacao_saque != "c" and confirmacao_saque != "a":
        print("\nValor inválido.")
        #Confirmar operação
        print(f"\nSacar R$ {valor_saque:.2f}.")
        confirmacao_saque = input("[c] Confirmar\n[a] Abortar\n")

    #Em caso de operação confirmada
    if confirmacao_saque == "c":
        contador += 1
        dia_da_ultima_operacao = date.today()
        saldo -= valor_saque
        saque_acumulado += valor_saque
        data = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        extrato += f"\n{data}\nSaque: R$ {valor_saque:.2f}\n"
        print("\n**Valor sacado com sucesso!**")

        return "menu", contador, dia_da_ultima_operacao, saque_acumulado, extrato

    #Em caso de operação abortada
    else:
        print("\nXX Operação abortada XX")
        return ("menu",)

def exibir_extrato(saldo, deposito_acumulado, *, saque_acumulado, extrato):

    #Variável apenas para fins de pausa de fluxo
    pausa = "a"

    while pausa != "m":
        print("\n"+extrato)
        print(f"Total de depósitos: R$ {deposito_acumulado:.2f}\nTotal de saques: R$ {saque_acumulado:.2f}\nSaldo: R$ {saldo:.2f}")
        pausa = input("-".center(30,"-") + "\n\n""Tecle [m] para Menu\n")

while True:
    
    opcao = input(menu)

    #Depósito
    if opcao == "d":

        primeiro, *resto = deposito(contador, dia_da_ultima_operacao, saldo, deposito_acumulado, extrato, LIMITE_OPERACOES)
        print(primeiro)
        print(resto)

        if primeiro == "menu":

            if resto != ():

                contador, dia_da_ultima_operacao, saldo, deposito_acumulado, extrato = resto
                continue

            else:

                continue

        elif primeiro == "encerrar":

            break
    
    #Saque
    elif opcao == "s":

        primeiro, *resto = saque(contador = contador, dia_da_ultima_operacao = dia_da_ultima_operacao, saldo = saldo, saque_acumulado = saque_acumulado, extrato = extrato, LIMITE_OPERACOES = LIMITE_OPERACOES, LIMITE_VALOR = LIMITE_VALOR)

        if primeiro == "menu":

            if resto != ():

                contador, dia_da_ultima_operacao, saque_acumulado, extrato = resto
                continue

            else:

                continue

        elif primeiro == "encerrar":

            break
    
    #Extrato
    elif opcao == "e":

        exibir_extrato(saldo, deposito_acumulado, saque_acumulado = saque_acumulado, extrato = extrato)

    #Fechar programa
    elif opcao == "q":
        break
    
    #Em caso de opção inválida
    else:

        print("\nOpção Inválida")
            