import sqlite3
from mcp.server.fastmcp import FastMCP
import json
import asyncio
from typing import Optional

mcp = FastMCP("MercadinhoAssistente")

def get_db_connection():
    conn = sqlite3.connect('loja_sistema.db')
    conn.row_factory = sqlite3.Row
    return conn

@mcp.tool()
def get_produtos_disponiveis():
    """Retorna os produtos disponíveis no mercadinho para comprar"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT produto_id, nome, descricao, categoria_id, valor FROM produtos")
        produtos = cursor.fetchall()
        conn.close()

        chaves = ["produto_id", "nome", "descricao", "categoria_id", "valor"]
        result = [dict(zip(chaves, tupla)) for tupla in produtos]
        return json.dumps(result, indent=4, sort_keys=True, default=str)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_lojas():
    """Retorna as lojas e suas informações de localização"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT loja_id, nome, cidade, estado, bairro FROM lojas")
        lojas = cursor.fetchall()
        conn.close()
        chaves = ["loja_id", "nome", "cidade", "estado", "bairro"]
        result = [dict(zip(chaves, tupla)) for tupla in lojas]
        return json.dumps(result, indent=4, sort_keys=True, default=str)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_categorias_produtos_promocao_por_loja(id_loja: int):
    """Retorna as categorias de produtos com promoções cadastradas nas lojas adquirintes"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            select p.loja_id,
                p2.produto_id,
                p2.nome, 
                c.categoria_id,
                c.nome,
                c.descricao
                p2.valor,
                p.desconto_loja, 
                p.desconto_socio
            from promocoes p
            join categorias c
                on p.categoria_id = c.categoria_id
            join produtos p2
                on c.categoria_id = p2.categoria_id
            where 1=1
            and p.loja_id = ?
            and p.ativa = 1""", (id_loja,))
        promocoes = cursor.fetchall()
        conn.close()

        chaves = ["loja_id", "produto_id", "nome", "categoria_id", "nome_categoria", "descricao", "valor", "desconto_loja", "desconto_socio"]
        result = [dict(zip(chaves, tupla)) for tupla in promocoes]
        return json.dumps(result, indent=4, sort_keys=True, default=str)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_promocao_por_loja(id_loja: int):
    """Retorna os produtos com promoções cadastradas nas lojas adquirintes"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        #cursor.execute("select p.loja_id, p.promocao_id, pp.produto_id, p.nome, p.descricao, p.desconto_loja, p.desconto_socio from promocoes p join promocoes_produtos pp on p.promocao_id = pp.promocao_id")
        cursor.execute("""
            select p.loja_id, 
                p.promocao_id, 
                p.produto_id, 
                p.categoria_id, 
                pp.nome, 
                pp.descricao,
                pp.valor,
                p.desconto_loja, 
                p.desconto_socio
            from promocoes p 
            join produtos pp 
                on p.produto_id = pp.produto_id 
            where 1=1
            and p.loja_id = ?
            and p.ativa = 1
            and p.categoria_id is null""", (id_loja,))
        promocoes = cursor.fetchall()
        conn.close()
        
        chaves = ["loja_id", "promocao_id", "produto_id", "categoria_id", "nome", "descricao", "valor", "desconto_loja", "desconto_socio"]
        #result = list(filter(lambda item: item[0] == str(id_loja), promocoes))
        result = [dict(zip(chaves, tupla)) for tupla in promocoes]
        #result = list(filter(lambda item: item["loja_id"] == str(id_loja), result))
        return json.dumps(result, indent=4, sort_keys=True, default=str)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_info_cliente(cliente_id: int, nome: str):
    """Retorna as informações do cliente pelo código e nome. Retonar se o cliente está na base de clientes socios que lhes concendem o direito a participar dos super descontos negociados."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT cliente_id, nome, sobrenome, cliente_socio, cidade, estado, cep, rua, numero, bairro, complemento FROM clientes WHERE cliente_id = ? AND nome||' '||sobrenome LIKE ?", (cliente_id, nome,))
        clientes = cursor.fetchall()
        conn.close()
        chaves = ["cliente_id", "nome", "sobrenome", "cliente_socio", "cidade", "estado", "cep", "rua", "numero", "bairro", "complemento"]
        result = [dict(zip(chaves, tupla)) for tupla in clientes]
        return json.dumps(result, indent=4, sort_keys=True, default=str)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def reservar_pedido_com_desconto(id_loja: int, id_cliente: int, data_hora: str):
    """Reservar para o cliente associado a compra de um item com desconto na loja"""
    try:
        # TODO: Implementar lógica de reserva no banco de dados
        # conn = get_db_connection()
        # cursor = conn.cursor()
        # cursor.execute("INSERT INTO reservas (loja_id, cliente_id, data_hora) VALUES (?, ?, ?)", 
        #                (id_loja, id_cliente, data_hora))
        # conn.commit()
        # conn.close()
        
        return {
            "message": "Reserva agendada com sucesso!",
            "loja_id": id_loja,
            "cliente_id": id_cliente,
            "data_hora": data_hora
        }
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def agenda_visita_para_compra(id_loja: int, data_hora: str):
    """Reservar a visita de um cliente na loja para conhecer melhor os nossos produtos"""
    try:
        # TODO: Implementar lógica de agendamento de visita
        # conn = get_db_connection()
        # cursor = conn.cursor()
        # cursor.execute("INSERT INTO visitas (loja_id, data_hora) VALUES (?, ?)", 
        #                (id_loja, data_hora))
        # conn.commit()
        # conn.close()
        return {
            "message": "Visita agendada com sucesso!",
            "loja_id": id_loja,
            "data_hora": data_hora
        }
    except Exception as e:
        return {"error": str(e)}
    
if __name__ == "__main__":
    # Para desenvolvimento local, usar stdio
    mcp.run(transport="stdio")
    
    # Para servidor remoto, usar HTTP streamable (recomendado para produção)
    # mcp.run(
    #     transport="http",
    #     host="127.0.0.1",
    #     port=4200,
    #     log_level="info"
    # )
