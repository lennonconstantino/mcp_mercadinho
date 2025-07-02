# Mercadinho Mercantes - Multi-Agent AI Assistant

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.45.0-red.svg)](https://streamlit.io/)
[![MCP](https://img.shields.io/badge/MCP-1.7.1-green.svg)](https://modelcontextprotocol.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)](https://openai.com/)

A sophisticated multi-agent AI system for Mercadinho Mercantes, a Brazilian retail chain. This system provides intelligent customer service through multiple specialized AI agents that can handle product inquiries, sales assistance, customer management, and store operations.

## 🏪 About Mercadinho Mercantes

Mercadinho Mercantes is a proud Brazilian retail company with multiple locations across São Paulo and Rio de Janeiro. Our AI assistant system enhances customer experience by providing personalized product recommendations, promotional information, and seamless appointment scheduling.

## ✨ Features

### 🤖 Multi-Agent Architecture
- **Reception Agent**: Welcomes customers and directs them to appropriate services
- **Sales Agent**: Handles product inquiries, recommendations, and sales assistance
- **Customer Maintenance Agent**: Manages existing customer accounts and special discounts

### 🛍️ Core Functionality
- **Product Catalog**: Browse available products with pricing and inventory
- **Store Information**: Find store locations and contact details
- **Promotional System**: Access store-specific promotions and discounts
- **Customer Management**: Track customer profiles and loyalty benefits
- **Appointment Scheduling**: Book store visits and product reservations
- **Special Discounts**: Exclusive offers for registered customers

### 🛠️ Technical Features
- **MCP Integration**: Model Context Protocol for tool calling
- **Streamlit UI**: Modern, responsive web interface
- **Real-time Chat**: Interactive conversation with AI agents
- **Tool Visualization**: Transparent view of AI tool usage
- **Session Management**: Persistent conversation history

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

### Running the Application

1. **Start the MCP server** (in one terminal):
   ```bash
   mcp run server.py --transport sse
   ```

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
  - Route customers to appropriate specialized agents
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
| `get_promocao_por_loja(id_loja)` | Get promotions for specific store | `id_loja: int` |
| `get_info_cliente(nome)` | Get customer information | `nome: str` |
| `reservar_pedido_com_desconto()` | Reserve order with discount | `id_loja, id_cliente, data_hora` |
| `agenda_visita_para_compra()` | Schedule store visit | `id_loja, data_hora` |

## 📊 Data Structure

### Products
- **Categories**: Hortifruit, Electronics
- **Information**: ID, name, category, price, quantity
- **Examples**: Bananas, Apples, PlayStation 5, LED TV

### Stores
- **Locations**: São Paulo (Parelheiros, Mooca), Guarujá, Santo André, Rio de Janeiro (Ipanema, Nova Iguaçu)
- **Information**: ID, name, city, state

### Customers
- **Types**: Regular customers, Members (with special discounts)
- **Information**: ID, name, associated store, discount eligibility

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
