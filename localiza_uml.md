#Este diagrama apresenta:
#Relação Cliente - Reserva: Cada cliente pode ter apenas uma reserva ativa.
#Relação Reserva - Carro: Cada reserva é associada a um carro.
#Subclasses de Carro: CarroEsportivo e CarroUtilitario, com atributos específicos.
#A classe Funcionario e Promocao como entidades independentes.


+------------------+        +-----------------+
|    Cliente       |<>------|    Reserva      |
+------------------+        +-----------------+
| - nome           |        | - codigo        |
| - cpf            |        | - status        |
| - idade          |        | - data_inicio   |
| - data_nascimento|        | - data_fim      |
| - numero_carteira|        | - carro         |<>-----+
| - foto_carteira  |        | - cliente       |
| - ano_vencimento |        +-----------------+
| - endereco       |
| - telefone       |                        +----------------+
| - email          |<>-----+                |     Carro      |
+------------------+        |                +----------------+
                            |                | - placa        |
                            |                | - ano          |
+------------------+        |                | - cor          |
|   Funcionario    |        |                | - modelo       |
+------------------+        |                | - quilometragem|
| - nome           |        |                | - valor_diario |
| - cpf            |        |                | - observacao   |
| - idade          |        |                +----------------+
| - endereco       |        |
| - data_contratacao|       |                +--------------------+
| - salario        |        |                |  CarroEsportivo   |
| - alugueis_realiz|        |                +--------------------+
| - status         |        |                | - tempo_100kmh     |
| - telefone       |        |                | - lista_melhorias  |
+------------------+        |                +--------------------+
                            |
                            |                +--------------------+
                            |                |  CarroUtilitario   |
                            |                +--------------------+
                            |                | - passageiros       |
                            |                | - tamanho_bagageiro |
                            |                | - km_por_litro      |
                            |                +--------------------+
                            |
                            +----------------+
                            |    Promocao    |
                            +----------------+
                            | - titulo       |
                            | - descricao    |
                            | - data_validade|
                            +----------------+
