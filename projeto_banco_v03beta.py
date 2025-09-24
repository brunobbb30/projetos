#Operações:
#   Geral
#       Limite de 10 transações por dia
#       Mensagem caso já tiver chegado ao limite de transações
#       (+) Inserir as operações de depósito, saque e extrato em funções
#           (+) Depósito: Função recebe argumentos apenas por posição
#           (+) Saque: Função recebe argumentos apenas por nome
#           (+) Extrato: Função recebe argumentos por posição (saldo) e por nome (extrato)
#       (+)Inserir funções de cadastro de usuários e cadastro de conta bancária (vincular com usuário)
#           (+)Usuário:
#               (+)armazenar em lista
#               (+)composto por: nome, data de nascimento, cpf, endereço
#                    (+)o endereço é uma string com o formato: logradouro, número - bairro - cidade/siglaEstado
#                    (+)cpf é somente números
#               (+)relação biunívoca entre cpf e usuário
#           (+)Conta:
#               (+)armazenar em lista
#               (+)composto por: agência, número da conta, usuário
#               (+)o número da conta é sequencial, iniciando em 1
#               (+)o número da agência é fixo: 0001
#               (+)o usuário pode ter mais de uma conta, mas uma conta pertence apenas a um usuário
#   Depositar
#       Somente valores positivos
#   Sacar
#       (-)Limite de 3 saques por dia
#       Somente valores positivos
#       Limite de 500 reais por saque
#       Mensagem caso a conta não tenha saldo
#   Extrato
#       Listar todos os depósitos e saques realizados
#       Exibir data e hora de cada operação
#       Exibir o saldo atual da conta
#       Valores com formato R$ xxx.xx

from abc import ABC, abstractmethod
from datetime import datetime

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo insuficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n *** Saque realizado com sucesso! ***")
            return True
        
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n*** Depósito realizado com sucesso! ***")

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque escede o limite. @@@")
        
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximos de saques excedido. @@@")

        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência: \t{self.agencia}
            C/C: \t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf

def filtrar_contas(cliente):
    contas_filtradas = None
    while not contas_filtradas:
        print("Suas contas:\n")
        for conta in cliente.contas:
            print(conta.numero)
        numero_conta_informado = input("\nInforme o número da conta desejada: ")

        contas_filtradas = [conta for conta in cliente.contas if conta.numero == numero_conta_informado]
        contas_filtradas = contas_filtradas[0]

        if not contas_filtradas:
            print("\nInforme uma conta existente: ")
    
    return contas_filtradas[0]

def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def login(clientes, contas):

    cpf = input("\nInforme seu cpf: ")
    cliente = filtrar_clientes(cpf, clientes)

    #Verificação se já é cliente
    if cliente:
        #Escolher conta
        if cliente.contas:
            conta = filtrar_contas(cliente)
            return conta

    else:
        cliente = criar_cliente(cpf, clientes)

        return criar_conta(cliente, contas)

def criar_cliente(cpf, clientes):
    nome = input("\nInforme seu nome: ")
    data_nascimento = input("\nInforme sua data de nascimento: ")

    logradouro = input("\nInforme seu logradouro: ")
    numero_da_residência = input("\nInforme o número da residência: ")
    bairro = input("\nInforme o bairro: ")
    cidade = input("\nInforme a cidade: ")
    estado = input("\nInforme o estado: ")
    endereco = f"{logradouro}, {numero_da_residência} - {bairro} - {cidade}/{estado}"

    cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)

    clientes.append(cliente)

    return cliente

def criar_conta(cliente, contas):
    numero_conta = len(contas) + 1
    #cliente = filtrar_clientes(cpf, clientes)
    conta = ContaCorrente.nova_conta(cliente, numero_conta)

    contas.append(conta)
    cliente.adicionar_conta(conta)

    return conta

def menu():
    menu = (f"""\n{" MENU ".center(30,"=")}
      
    Tecle [d] para depositar
      
    Tecle [s] para sacar
      
    Tecle [e] para extrato
            
    Tecle [c] para trocar de conta
            
    Tecle [u] para trocar de usuário
    
    Tecle [q] para sair
        
""")
    
    return input(menu)

def depositar(conta):
    valor = float(input("\nDigite o valor a ser depositado: R$ "))
    transacao = Deposito(valor)
    cliente = conta.cliente
    cliente.realizar_transacao(conta, transacao)

def sacar(conta):
    valor = float(input("\nDigite o valor a ser sacado: R$ "))
    transacao = Saque(valor)
    cliente = conta.cliente
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(conta):
    historico_transacoes = conta.historico.transacoes

    if not historico_transacoes:
        print("Nenhuma transação realizada.")

    else:
        extrato = ""
        for transacao in historico_transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

def main():
    clientes = []
    contas = []

    while True:
        
        conta = login(clientes, contas)

        while True:

            opcao = menu()

            if opcao == "d":
                depositar(conta)
            elif opcao == "s":
                sacar(conta)
            elif opcao == "e":
                exibir_extrato(conta)
            elif opcao == "c":
                cliente = conta.cliente
                conta = filtrar_contas(cliente)
            elif opcao == "u":
                conta = login(clientes, contas)
            elif opcao == "q":
                break
            else:
                print("\nOpção Inválida")
        
        break

main()