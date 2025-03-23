import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    cliente_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf_cliente VARCHAR(11) NOT NULL,
    nome_cliente VARCHAR(50) NOT NULL,
    email_cliente VARCHAR(50) NOT NULL,
    telefone_cliente VARCHAR(11) NOT NULL
);""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS categoria (
    categoria_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_categoria VARCHAR(50) NOT NULL
);""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS fornecedor (
    fornecedor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_fornecedor VARCHAR(50) NOT NULL,
    cnpj_fornecedor VARCHAR(14) NOT NULL,
    email_fornecedor VARCHAR(50) NOT NULL,
    telefone_fornecedor VARCHAR(11) NOT NULL
);""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS mercado (
    mercado_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_mercado VARCHAR(50) NOT NULL,
    cnpj_mercado VARCHAR(14) NOT NULL,
    email_mercado VARCHAR(50) NOT NULL,
    telefone_mercado VARCHAR(11) NOT NULL
);""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS produto (
    produto_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_produto VARCHAR(50) NOT NULL,
    preco_produto FLOAT NOT NULL,
    estoque_produto INTEGER NOT NULL,
    id_mercado INTEGER NOT NULL,
    id_fornecedor INTEGER NOT NULL,
    id_categoria INTEGER NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categoria (categoria_id),
    FOREIGN KEY (id_mercado) REFERENCES mercado (mercado_id),
    FOREIGN KEY (id_fornecedor) REFERENCES fornecedor (fornecedor_id)
);""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionario (
    funcionario_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_funcionario VARCHAR(50) NOT NULL,
    cpf_funcionario VARCHAR(11) NOT NULL,
    email_funcionario VARCHAR(50) NOT NULL,
    telefone_funcionario VARCHAR(11) NOT NULL,
    id_mercado INTEGER NOT NULL,
    FOREIGN KEY (id_mercado) REFERENCES mercado (mercado_id)
);""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS venda (
    venda_id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE NOT NULL,
    valor_venda FLOAT NOT NULL,
    id_cliente INTEGER NOT NULL,
    id_funcionario INTEGER NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes (cliente_id),
    FOREIGN KEY (id_funcionario) REFERENCES funcionario (funcionario_id)
);""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pagamento (
    pagamento_id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_pagamento DATE NOT NULL,
    valor_pagamento FLOAT NOT NULL,
    tipo_pagamento VARCHAR(50) NOT NULL,
    id_venda INTEGER NOT NULL,
    FOREIGN KEY (id_venda) REFERENCES venda (venda_id)
);""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS detalhe_venda (
    id_produto INTEGER NOT NULL,
    id_venda INTEGER NOT NULL,
    quantidade_produto INTEGER NOT NULL,
    valor_produto FLOAT NOT NULL,
    status_produto VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_produto) REFERENCES produto (produto_id),
    FOREIGN KEY (id_venda) REFERENCES venda (venda_id)
);""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS endereco_cliente (
    endereco_id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    cep_cliente VARCHAR(8) NOT NULL,
    rua_cliente VARCHAR(50) NOT NULL,
    numero_cliente INTEGER NOT NULL,
    bairro_cliente VARCHAR(50) NOT NULL,
    cidade_cliente VARCHAR(50) NOT NULL,
    estado_cliente VARCHAR(2) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes (cliente_id)
);""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS endereco_mercado (
    endereco_id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_mercado INTEGER NOT NULL,
    cep_mercado VARCHAR(8) NOT NULL,
    rua_mercado VARCHAR(50) NOT NULL,
    numero_mercado INTEGER NOT NULL,
    bairro_mercado VARCHAR(50) NOT NULL,
    cidade_mercado VARCHAR(50) NOT NULL,
    estado_mercado VARCHAR(2) NOT NULL,
    FOREIGN KEY (id_mercado) REFERENCES mercado (mercado_id)
);""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS endereco_fornecedor (
    endereco_id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_fornecedor INTEGER NOT NULL,
    cep_fornecedor VARCHAR(8) NOT NULL,
    rua_fornecedor VARCHAR(50) NOT NULL,
    numero_fornecedor INTEGER NOT NULL,
    bairro_fornecedor VARCHAR(50) NOT NULL,
    cidade_fornecedor VARCHAR(50) NOT NULL,
    estado_fornecedor VARCHAR(2) NOT NULL,
    FOREIGN KEY (id_fornecedor) REFERENCES fornecedor (fornecedor_id)
);""")


conn.commit()
conn.close()

print("Tabelas criadas com sucesso!")
