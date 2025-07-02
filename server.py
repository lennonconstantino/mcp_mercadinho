from mcp.server.fastmcp import FastMCP
import json

mcp = FastMCP("MercadinhoAssistente")

@mcp.tool()
def get_produtos_disponiveis():
    """Retorna os produtos disponíveis no mercadinho para comprar"""
    try:
        produtos = [
            {
                "id_produto": "1",
                "nome": "banana",
                "categoria": "hortifruit",
                "valor": 10.0,
                "quantidade":100,
            },
            {
                "id_produto": "2",
                "nome": "maca",
                "categoria": "hortifruit",
                "valor": 12.0,
                "quantidade":500,
            },
            {
                "id_produto": "3",
                "nome": "pera",
                "categoria": "hortifruit",
                "valor": 12.4,
                "quantidade":150,
            },
            {
                "id_produto": "4",
                "nome": "mamao",
                "categoria": "hortifruit",
                "valor": 15.0,
                "quantidade":130,
            },
            {
                "id_produto": "5",
                "nome": "playstation 5",
                "categoria": "eletronico",
                "valor": 3500.0,
                "quantidade":30,
            },
            {
                "id_produto": "6",
                "nome": "televisao led",
                "categoria": "eletronico",
                "valor": 5500.0,
                "quantidade":10,
            },
        ]
        return json.dumps(produtos, indent=4, sort_keys=True, default=str)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_lojas():
    """Retorna as lojas e suas informações de localização"""
    try:
        lojas = [
            {
                "id_loja" : "1",
                "nome": "loja Parelheiros",
                "cidade": "São Paulo",
                "estado": "São Paulo",
            },
            {
                "id_loja" : "2",
                "nome": "loja Guaruja",
                "cidade": "Guaruja",
                "estado": "São Paulo",
            },
            {
                "id_loja" : "3",
                "nome": "loja Santo Andre",
                "cidade": "Santo Andre",
                "estado": "São Paulo",
            },
            {
                "id_loja" : "4",
                "nome": "loja Mooca",
                "cidade": "São Paulo",
                "estado": "São Paulo",
            },
            {
                "id_loja" : "5",
                "nome": "loja Ipanema",
                "cidade": "Rio de Janeiro",
                "estado": "Rio de Janeiro",
            },
            {
                "id_loja" : "6",
                "nome": "loja Nova Iguaçu",
                "cidade": "Nova Iguaçu",
                "estado": "Rio de Janeiro",
            },
        ]
        return json.dumps(lojas, indent=4, sort_keys=True, default=str)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_promocao_por_loja(id_loja: int):
    """Retorna as promoções cadastradas nas lojas adquirintes"""
    try:
        promocoes = [
            {
                "id_loja" : "1",
                "items": [
                    { 
                        "id_produto":"1",
                        "nome": "banana",
                        "desconto": "10%"
                    },
                    { 
                        "id_produto":"5",
                        "nome": "playstation 5",
                        "desconto": "20%"
                    },
                ]
            },
            {
                "id_loja" : "4",
                "items": [
                    { 
                        "id_produto":"5",
                        "nome": "playstation 5",
                        "desconto": "20%"
                    },
                    { 
                        "id_produto":"6",
                        "nome": "televisao led",
                        "desconto": "30%"
                    },
                ]
            },      
        ]
        result = list(filter(lambda item: item["id_loja"] == str(id_loja), promocoes))
        return json.dumps(result, indent=4, sort_keys=True, default=str)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def get_info_cliente(nome: str):
    """Retorna as informações do cliente pelo nome. Retonar se o cliente está na base de clientes socios que lhes concendem o direito a participar dos super descontos negociados."""
    try:
        clientes = [
            {
                "id_cliente": "1",
                "nome": "John Lennon",
                "id_loja" : "1",
                "nome_loja": "loja Parelheiros",
                "descontos": True,
                "cidade": "São Paulo",
                "estado": "São Paulo",
            },
            {
                "id_cliente": "2",
                "nome": "Mary Anne",
                "id_loja" : "1",
                "nome_loja": "loja Parelheiros",
                "descontos": True,
                "cidade": "São Paulo",
                "estado": "São Paulo",
            },
            {
                "id_cliente": "3",
                "nome": "Jesus Christ",
                "id_loja" : "1",
                "nome_loja": "loja Parelheiros",
                "descontos": True,
                "cidade": "São Paulo",
                "estado": "São Paulo",
            },
            {
                "id_cliente": "4",
                "nome": "Giovanni Martinelli",
                "id_loja" : "4",
                "nome_loja": "loja Mooca",
                "descontos": True,
                "cidade": "São Paulo",
                "estado": "São Paulo",
            },
            {
                "id_cliente": "4",
                "nome": "Heinz Krauss",
                "id_loja" : "4",
                "nome_loja": "loja Mooca",
                "descontos": False,
                "cidade": "São Paulo",
                "estado": "São Paulo",
            },
        ]
        result = list(filter(lambda item: item["nome"] == str(nome), clientes))
        return json.dumps(result, indent=4, sort_keys=True, default=str)
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def reservar_pedido_com_desconto(id_loja: int, id_cliente: int, data_hora: str):
    """Reservar para o cliente associado a compra de um item com desconto na loja"""
    try:
        return {"message": "Reserva agendada com sucesso!"}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def agenda_visita_para_compra(id_loja: int, data_hora: str):
    """Reservar a visita de um cliente na loja para conhecer melhor os nossos produtos"""
    try:
        # TODO
        return {"message": "Reserva agendada com sucesso!"}
    except Exception as e:
        return {"error": str(e)}
    
