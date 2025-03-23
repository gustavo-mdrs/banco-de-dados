import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Inserir dados na tabela clientes
cursor.execute("INSERT INTO clientes (cpf_cliente, nome_cliente, email_cliente, telefone_cliente) VALUES ('12345678901', 'Alice Silva', 'alice@email.com', '11987654321')")
cursor.execute("INSERT INTO clientes (cpf_cliente, nome_cliente, email_cliente, telefone_cliente) VALUES ('98765432100', 'Carlos Souza', 'carlos@email.com', '21987654321')")

# Inserir dados na tabela fornecedor
cursor.execute("INSERT INTO fornecedor (nome_fornecedor, cnpj_fornecedor, email_fornecedor, telefone_fornecedor) VALUES ('Fornecedor A', '12345678000199', 'fornecedorA@email.com', '31987654321')")

# Inserir dados na tabela mercado
cursor.execute("INSERT INTO mercado (nome_mercado, cnpj_mercado, email_mercado, telefone_mercado) VALUES ('Supermercado X', '98765432000188', 'mercadoX@email.com', '41987654321')")

# Inserir dados na tabela categoria
cursor.execute("INSERT INTO categoria (nome_categoria) VALUES ('Eletrônicos')")
cursor.execute("INSERT INTO categoria (nome_categoria) VALUES ('Alimentos')")

# Inserir dados na tabela produto
cursor.execute("INSERT INTO produto (nome_produto, preco_produto, estoque_produto, id_mercado, id_fornecedor, id_categoria) VALUES ('TV 50 Polegadas', 5500.00, 10, 1, 1, 1)")
cursor.execute("INSERT INTO produto (nome_produto, preco_produto, estoque_produto, id_mercado, id_fornecedor, id_categoria) VALUES ('Arroz 5kg', 20.00, 50, 1, 1, 2)")

# Inserir dados na tabela funcionario
cursor.execute("INSERT INTO funcionario (nome_funcionario, cpf_funcionario, email_funcionario, telefone_funcionario, id_mercado) VALUES ('João Oliveira', '11122233344', 'joao@email.com', '51987654321', 1)")

# Inserir dados na tabela venda
cursor.execute("INSERT INTO venda (data_venda, valor_venda, id_cliente, id_funcionario) VALUES ('2025-03-17', 2520.00, 1, 1)")

# Inserir dados na tabela pagamento
cursor.execute("INSERT INTO pagamento (data_pagamento, valor_pagamento, tipo_pagamento, id_venda) VALUES ('2025-03-17', 2520.00, 'Cartão de Crédito', 1)")

# Inserir dados na tabela detalhe_venda
cursor.execute("INSERT INTO detalhe_venda (id_produto, id_venda, quantidade_produto, valor_produto, status_produto) VALUES (1, 1, 1, 2500.00, 'Entregue')")
cursor.execute("INSERT INTO detalhe_venda (id_produto, id_venda, quantidade_produto, valor_produto, status_produto) VALUES (2, 1, 1, 20.00, 'Entregue')")

# Inserir dados na tabela endereco_cliente
cursor.execute("INSERT INTO endereco_cliente (id_cliente, cep_cliente, rua_cliente, numero_cliente, bairro_cliente, cidade_cliente, estado_cliente) VALUES (1, '01001000', 'Rua A', 100, 'Centro', 'São Paulo', 'SP')")

# Inserir dados na tabela endereco_mercado
cursor.execute("INSERT INTO endereco_mercado (id_mercado, cep_mercado, rua_mercado, numero_mercado, bairro_mercado, cidade_mercado, estado_mercado) VALUES (1, '02002000', 'Rua B', 200, 'Centro', 'São Paulo', 'SP')")

# Inserir dados na tabela endereco_fornecedor
cursor.execute("INSERT INTO endereco_fornecedor (id_fornecedor, cep_fornecedor, rua_fornecedor, numero_fornecedor, bairro_fornecedor, cidade_fornecedor, estado_fornecedor) VALUES (1, '03003000', 'Rua C', 300, 'Industrial', 'Belo Horizonte', 'MG')")


conn.commit()
conn.close()

print("Dados inseridos com sucesso!")
