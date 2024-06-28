class Cliente:
    def __init__(self, nome, cpf, idade, endereco):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.endereco = endereco
        self.senha_registrada = None

    def informacoes(self):
        return f'CPF: {self.cpf}, Nome: {self.nome}, Idade: {self.idade}, Endereço: {self.endereco}'

    def registrar_senha(self):
        self.senha_registrada = input('Crie sua senha: ')
        print('Senha registrada com sucesso!')

class Conta:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = saldo

    def autenticar(self):
        senha = input('Digite a sua senha: ')
        return senha == self.cliente.senha_registrada

    def depositar(self, valor):
        if self.autenticar():
            if valor > 0:
                self.saldo += valor
                print(f'O valor de R${valor} foi adicionado ao saldo.')
            else:
                print('Valor inválido!')
        else:
            print('Autenticação falhou!')

    def saque(self, valor):
        if self.autenticar():
            if 0 < valor <= self.saldo:
                self.saldo -= valor
                print(f'Valor de R${valor} retirado com sucesso!')
            else:
                print('Valor de saque inválido ou saldo insuficiente!')
        else:
            print('Autenticação falhou!')

    def verificar_saldo(self):
        if self.autenticar():
            return f'Saldo atual: R${self.saldo}'
        else:
            return 'Autenticação falhou!'

# Solicitando informações do usuário
nome = input('Digite seu nome: ')
cpf = input('Digite seu CPF: ')
idade = int(input('Digite sua idade: '))
endereco = input('Digite seu endereço: ')

# Criando uma instância de Cliente
cliente1 = Cliente(nome, cpf, idade, endereco)
cliente1.registrar_senha()

# Criando uma instância de Conta associada ao cliente
conta1 = Conta(cliente1)

# Exemplo de uso
print(cliente1.informacoes())
conta1.depositar(500)
print(conta1.verificar_saldo())
conta1.saque(200)
print(conta1.verificar_saldo())
