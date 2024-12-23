#Representa um cliente do sistema
class Cliente:
    def __init__(self, nome, cpf, idade, data_nascimento, numero_carteira, foto_carteira, ano_vencimento, endereco, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.data_nascimento = data_nascimento
        self.numero_carteira = numero_carteira
        self.foto_carteira = foto_carteira
        self.ano_vencimento = ano_vencimento
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.reserva = None

#Retorna a reserva associada ao cliente.
    def get_reservas(self):
        return self.reserva

#Representa um funcionário do sistema.
class Funcionario:
    def __init__(self, nome, cpf, idade, endereco, data_contratacao, salario, alugueis_realizados, status, telefone):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.endereco = endereco
        self.data_contratacao = data_contratacao
        self.salario = salario
        self.alugueis_realizados = alugueis_realizados
        self.status = status
        self.telefone = telefone

#Representa um carro genérico disponível para locação.
class Carro:
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diario, observacao):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.modelo = modelo
        self.quilometragem = quilometragem
        self.valor_diario = valor_diario
        self.observacao = observacao

#Representa um carro esportivo.
class CarroEsportivo(Carro):
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diario, observacao, tempo_100kmh, lista_melhorias):
        super().__init__(placa, ano, cor, modelo, quilometragem, valor_diario, observacao)
        self.tempo_100kmh = tempo_100kmh
        self.lista_melhorias = lista_melhorias

#Representa um carro utilitário.
class CarroUtilitario(Carro):
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diario, observacao, passageiros, tamanho_bagageiro, km_por_litro):
        super().__init__(placa, ano, cor, modelo, quilometragem, valor_diario, observacao)
        self.passageiros = passageiros
        self.tamanho_bagageiro = tamanho_bagageiro
        self.km_por_litro = km_por_litro

#Representa uma reserva de locação de carro.
class Reserva:
    def __init__(self, codigo, status, data_inicio, data_fim, carro, cliente):
        self.codigo = codigo
        self.status = status
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.carro = carro
        self.cliente = cliente

#Calcula o custo total da reserva com base na quantidade de dias e no valor diário do carro.
    def calcular_valor(self):
        dias = (self.data_fim - self.data_inicio).days
        return dias * self.carro.valor_diario

#Representa uma promoção que pode ser enviada aos clientes.
class Promocao:
    def __init__(self, titulo, descricao, data_validade):
        self.titulo = titulo
        self.descricao = descricao
        self.data_validade = data_validade
