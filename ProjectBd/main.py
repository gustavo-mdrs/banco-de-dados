import sqlite3
import pandas as pd

conn = sqlite3.connect("database.db")

queries = {
    "Clientes": "SELECT * FROM clientes;",
    "Vendas e Clientes": """
        SELECT venda.venda_id, venda.data_venda, venda.valor_venda, clientes.nome_cliente 
        FROM venda
        JOIN clientes ON venda.id_cliente = clientes.cliente_id;
    """,
    "Produtos com Estoque Baixo": "SELECT * FROM produto WHERE estoque_produto < 10;",
    "Vendas por Funcionário": """
        SELECT funcionario.nome_funcionario, COUNT(venda.venda_id) AS total_vendas
        FROM venda
        JOIN funcionario ON venda.id_funcionario = funcionario.funcionario_id
        GROUP BY funcionario.nome_funcionario
        ORDER BY total_vendas DESC;
    """,
    "Produtos Mais Vendidos": """
        SELECT produto.nome_produto, SUM(detalhe_venda.quantidade_produto) AS total_vendido
        FROM detalhe_venda
        JOIN produto ON detalhe_venda.id_produto = produto.produto_id
        GROUP BY produto.nome_produto
        ORDER BY total_vendido DESC
        LIMIT 5;
    """
}

for descricao, query in queries.items():
    try:
        df = pd.read_sql_query(query, conn)
        print(f"\n=== {descricao} ===")
        print(df if not df.empty else "Nenhum dado encontrado.")
    except Exception as e:
        print(f"\nErro ao executar {descricao}: {e}")


conn.close()
