from agents import Agent, ModelSettings, Runner
from agents.mcp import MCPServerStdio 
import streamlit as st
from dotenv import load_dotenv
import asyncio, json, sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

st.markdown("<h1 style='text-align: center;'>Mercadinho Mercantes</h1>", unsafe_allow_html=True)

_, cent_co, _ = st.columns(3)
with cent_co:
    st.image("images/Gemini_Generated_Image_kmsn80kmsn80kmsn.png", caption="Mercadinho Mercantes")

if "history" not in st.session_state:
    load_dotenv()  
    st.session_state.history = []

for message in st.session_state.history:
    type = message.get("role", None) or message.get("type", None)

    match type:
        case 'user': 
            with st.chat_message(type):
                st.markdown(message["content"])
        case 'assistant': 
            with st.chat_message(type):
                st.markdown(message["content"][0]["text"])
        case 'function_call': 
            if "transfer_to" not in message["name"]: 
                with st.chat_message(name="tool", avatar=":material/build:"):
                        st.markdown(f'LLM chamando tool {message["name"]}')
                        with st.expander("Visualizar argumentos"):
                            st.code(message["arguments"])
        case 'function_call_output':
            try:
                obj = json.loads(message['output'])
                with st.chat_message(name="tool", avatar=":material/data_object:"):
                    with st.expander("Visualizar resposta"):
                        st.code(obj["text"])
            except:
                continue

if "agentRecepcao" not in st.session_state: 
        agenteManutencaoSocio = Agent( 
            name="ManutencaoSocioAssistente", 
            model="gpt-4-1106-preview",
            handoff_description="Assistente de compra/consulta para clientes que já possuem carteira de sócio.",
            instructions="Você é um assistente da Mercadinho Mercantes que deve ajudar o cliente a consultar produtos e promoções." \
                "Pergunte o nome completo para identificar o cliente e então use as ferramentas para descobrir os produtos e promoções que tem (get_info_cliente). " \
                "Com base nisso colete as informações do que ele precisa, agende um horário na loja para ele comprar um produto com desconto especial (com reservar_pedido_com_desconto)." \
                "Não é necessario escolher uma loja especifica, apenas agendar a visita na loja onde comprou o produtos. ",
            model_settings=ModelSettings(tool_choice="auto", temperature=0, parallel_tool_calls=False), 
        )

        agentVendas = Agent(  
            name="VendasAssistente", 
            model="gpt-4-1106-preview",
            handoff_description="Assistente para trativa de vendas, informações sobre produtos e agendamento de visitas e reservas de pedidos com descontos.",
            instructions="Você é um assistente da Mercadinho Mercantes que deve ajudar e convencer o cliente a comprar um produto." \
                "Antes de tudo use a ferramenta get_produtos_disponiveis ou a ferramenta get_categorias_produtos_promocao_por_loja conforme a necessidade para conhecer as opções disponíveis e apresentar a ele. " \
                "Você pode fazer perguntas para entender o que o cliente precisa e oferecer as melhores opções de produtos baseado na ferramenta que você chamou. " \
                "Quando o cliente decidir, agende uma visita na loja mais próxima do cliente, para descobrir as lojas use get_lojas " \
                "e para descobrir os itens/produtos dessa loja use get_promoção_por_loja. " \
                "Se o cliente tiver a flag de desconto ativada, conceder mais 10%% de desconto sobre o valor do produto."
                "Então, agende a visita com a ferramenta agenda_visita_para_compra, onde você vai escolher a loja mais próxima do cliente.",
            model_settings=ModelSettings(tool_choice="auto", temperature=0, parallel_tool_calls=False), 
        )

        agentRecepcao = Agent( 
            name="RecepcaoAssistente", 
            model="gpt-4-1106-preview",
            handoffs=[agentVendas, agenteManutencaoSocio], 
            instructions="Você é um assistente de recepção da Mercadinho Mercantes, uma empresa nacional de Varejo do Brasil." \
                "Você é responsável pela recepção e deve apenas apresentar a empresa e oferecer as opções disponíveis. " \
                "Apresente a Mercadinho Mercantes como empresa de varejo e orgulhosamente brasileira." \
                "Mostre o site https://www.mecadinhomercantes.com.br/ para conhecer mais sobre a empresa." \
                "Ofereça para conhecer os produtos e agendar uma visita nas lojas com possibilidade de provar e experimentar os produtos se possível." \
                "Ou então no caso de querer troca ou revisão pode agendar uma visita a loja.",
            model_settings=ModelSettings(tool_choice="auto", temperature=0, parallel_tool_calls=False), 
        )

        st.session_state.agentRecepcao = agentRecepcao
        st.session_state.agentVendas = agentVendas
        st.session_state.agenteManutencaoSocio = agenteManutencaoSocio
        st.session_state.current_agent = agentRecepcao 

async def resolve_chat(): 
    async with MCPServerStdio(params={"command": "mcp", "args": ["run", "server.py"]}) as server:
        st.session_state.agentVendas.mcp_servers = [server] 
        st.session_state.agenteManutencaoSocio.mcp_servers = [server] 

        result = await Runner.run(
            starting_agent=st.session_state.current_agent, 
            input=st.session_state.history, 
            context=st.session_state.history
        )
       
        st.session_state.current_agent = result.last_agent
        st.session_state.history = result.to_input_list()
      
prompt = st.chat_input("Digite sua pergunta:")

if prompt:
    st.session_state.history.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Pensando..."):
        asyncio.run(resolve_chat())
        st.rerun()

if "current_agent" in st.session_state: 
    st.toast(f"Agente atual: { st.session_state.current_agent.name }")

