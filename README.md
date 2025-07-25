# Mercadinho Mercantes - Multi-Agent AI Assistant

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.45.0-red.svg)](https://streamlit.io/)
[![MCP](https://img.shields.io/badge/MCP-1.7.1-green.svg)](https://modelcontextprotocol.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)](https://openai.com/)

A multi-agent AI system for Mercadinho Mercantes, a Brazilian retail chain. This system provides intelligent customer service through specialized AI agents that handle product inquiries, sales assistance, customer management, and store operations.

## 🏪 About Mercadinho Mercantes

Mercadinho Mercantes is a Brazilian retail company with multiple locations. This AI assistant system enhances customer experience by providing product recommendations, promotional information, and appointment scheduling.

## ✨ Features

### 🤖 Multi-Agent Architecture
- **Reception Agent**: Welcomes customers and directs them to appropriate services
- **Sales Agent**: Handles product inquiries, recommendations, and sales assistance
- **Customer Maintenance Agent**: Manages customer accounts and special discounts

### 🛍️ Core Functionality
- Product catalog browsing
- Store information lookup
- Promotional system (store-specific)
- Customer management and loyalty benefits
- Appointment scheduling for store visits and product reservations
- Special discounts for registered customers

### 🛠️ Technical Features
- MCP (Model Context Protocol) integration for tool calling
- Streamlit UI for interactive chat
- Real-time chat with AI agents
- Tool usage visualization
- Session management

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API key
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mcp_mercadinho
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   export OPENAI_API_KEY="your_openai_api_key_here"
   ```
   Or create a `.env` file:
   ```bash
   echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
   ```

4. **Database setup**
   - The application requires a pre-existing `loja_sistema.db` SQLite database with the correct schema. If you do not have this file, please request the schema or a setup script from the project maintainer. (The setup script is not included in this repository.)

### Running the Application

1. **Start the MCP server** (in one terminal):
   ```bash
   python server.py
   ```
   (By default, runs with stdio transport for local development.)

2. **Launch the Streamlit client** (in another terminal):
   ```bash
   streamlit run chat_multi_agent_client.py
   ```

3. **Open your browser** and navigate to the URL shown in the Streamlit output (typically `http://localhost:8501`)

## 🏗️ Architecture

### System Components

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Streamlit UI  │◄──►│  Multi-Agent     │◄──►│   MCP Server    │
│   (Frontend)    │    │  System          │    │   (Backend)     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │  OpenAI GPT-4    │
                       │  (LLM Backend)   │
                       └──────────────────┘
```

### Agent Roles

#### Reception Agent (`RecepcaoAssistente`)
- **Purpose**: Initial customer contact and routing
- **Responsibilities**:
  - Welcome customers to Mercadinho Mercantes
  - Present company information and website
  - Route customers to specialized agents
  - Handle general inquiries

#### Sales Agent (`VendasAssistente`)
- **Purpose**: Product sales and recommendations
- **Responsibilities**:
  - Show available products and inventory
  - Provide product recommendations
  - Handle promotional offers
  - Schedule store visits
  - Process sales inquiries

#### Customer Maintenance Agent (`ManutencaoSocioAssistente`)
- **Purpose**: Existing customer support and loyalty management
- **Responsibilities**:
  - Verify customer membership status
  - Apply special discounts for members
  - Handle product reservations
  - Manage customer accounts

### Available Tools (MCP Functions)

| Tool | Description | Parameters |
|------|-------------|------------|
| `get_produtos_disponiveis()` | Retrieve available products | None |
| `get_lojas()` | Get store locations and information | None |
| `get_categorias_produtos_promocao_por_loja(id_loja)` | Get categories with promotions for a store | `id_loja: int` |
| `get_promocao_por_loja(id_loja)` | Get product promotions for a store | `id_loja: int` |
| `get_info_cliente(cliente_id, nome)` | Get customer information | `cliente_id: int, nome: str` |
| `reservar_pedido_com_desconto(id_loja, id_cliente, data_hora)` | Reserve order with discount | `id_loja: int, id_cliente: int, data_hora: str` |
| `agenda_visita_para_compra(id_loja, data_hora)` | Schedule store visit | `id_loja: int, data_hora: str` |

## 📊 Data Structure (Example)

### Products
- **Fields**: produto_id, nome, descricao, categoria_id, valor

### Stores
- **Fields**: loja_id, nome, cidade, estado, bairro

### Customers
- **Fields**: cliente_id, nome, sobrenome, cliente_socio, cidade, estado, cep, rua, numero, bairro, complemento

## 🎯 Usage Examples

### Product Inquiry
```
User: "What products do you have available?"
Agent: [Shows product catalog with prices and availability]
```

### Store Visit Scheduling
```
User: "I want to visit a store to see the PlayStation 5"
Agent: [Finds nearest store, checks promotions, schedules visit]
```

### Customer Discount Check
```
User: "My name is John Lennon, do I have any special discounts?"
Agent: [Verifies membership, applies special pricing]
```

## 🔧 Configuration

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key for GPT-4 access

### Model Settings
- **Model**: GPT-4-1106-preview
- **Temperature**: 0 (deterministic responses)
- **Tool Choice**: Auto
- **Parallel Tool Calls**: Disabled

## 🛡️ Security Considerations

- API keys should be stored securely in environment variables
- Never commit API keys to version control
- Use `.env` files for local development
- Consider implementing rate limiting for production use

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Check the [Issues](https://github.com/your-repo/issues) page
- Contact the development team
- Visit [Mercadinho Mercantes](https://www.mecadinhomercantes.com.br/)

## 🔮 Future Enhancements

- [ ] Integration with real inventory systems
- [ ] Payment processing capabilities
- [ ] Multi-language support (Portuguese/English)
- [ ] Mobile app development
- [ ] Advanced analytics and reporting
- [ ] Integration with CRM systems

---

**Built with ❤️ for Mercadinho Mercantes**
