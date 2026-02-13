
<img width="1481" height="477" alt="logo0" src="https://github.com/user-attachments/assets/efc12b02-9995-4a40-980a-68da7d0feadd" />

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)

An intelligent AI agent powered by large language models with multi-tool integration for web search, Wikipedia queries, web scraping, calculations, and more.

[Features](#features) • [Demo](#demo) • [Installation](#installation) • [Usage](#usage) • [API Reference](#api-reference) • [Contributing](#contributing)

</div>

---

## 🌟 Overview

**AgentGo** is an advanced AI agent framework that combines the power of large language models (LLMs) with a comprehensive set of tools. It can intelligently decide which tools to use based on user queries, execute multiple tool calls, and provide comprehensive responses.

The agent uses a function-calling approach where the LLM determines which tools are needed, executes them, and synthesizes the results into coherent responses.

---
<img width="1174" height="728" alt="img0 1" src="https://github.com/user-attachments/assets/384d9774-ac59-427c-85c5-c0e17bbb3bce" />


## CLI interface

<img width="1223" height="892" alt="img2" src="https://github.com/user-attachments/assets/8ab80fca-e33d-4538-9881-1d816d0ef10e" />

```
┌──────────────────────────────────────────────────────────────────────────┐
│                           EXAMPLE EXECUTION FLOW                         │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  User: "What's the population of Tokyo and calculate its density?"       │
│                                                                          │
│  Iteration 1:                                                            │
│  ├─ LLM decides: Need wikipedia_search("Tokyo population")               │
│  ├─ Tool executes → Returns: "Tokyo has 14 million people, 2,194 km²"    │
│  └─ Append to conversation                                               │
│                                                                          │
│  Iteration 2:                                                            │
│  ├─ LLM decides: Need calculator("14000000 / 2194")                      │
│  ├─ Tool executes → Returns: "6380.4"                                    │
│  └─ Append to conversation                                               │
│                                                                          │
│  Iteration 3:                                                            │
│  ├─ LLM decides: Have all info, provide final answer                     │
│  └─ Returns: "Tokyo has a population of 14 million people across         │
│              2,194 km², giving it a density of ~6,380 people/km²"        │
│                                                                          │
│  Total iterations: 3                                                     │
│  Tools used: wikipedia_search, calculator                                │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```
---

## 🚀 Installation

### Prerequisites

- Python 3.11 or higher
- Docker (optional, for containerized deployment)
- Groq API Key (required for LLM functionality)

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/agentgo.git
   cd agentgo
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the application**
   
   **Option 1: Web Interface**
   ```bash
   python app.py
   ```
   Then open your browser and navigate to `http://localhost:5000`

   **Option 2: Command Line Interface**
   ```bash
   python main.py
   ```

### Docker Setup

1. **Build the Docker image**
   ```bash
   docker build -t agentgo .
   ```

2. **Run the container**
   ```bash
   docker run -d \
     -p 5000:5000 \
     -e GROQ_API_KEY=your_groq_api_key_here \
     --name agentgo \
     agentgo
   ```

3. **Access the application**
   
   Open your browser and navigate to `http://localhost:5000`

**Using Docker Compose (Recommended)**

Create a `docker-compose.yml` file:

```yaml
version: '3.8'

services:
  agentgo:
    build: .
    ports:
      - "5000:5000"
    environment:
      - GROQ_API_KEY=${GROQ_API_KEY}
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "python", "-c", "import requests; requests.get('http://localhost:5000/', timeout=2)"]
      interval: 30s
      timeout: 10s
      retries: 3
```

Then run:
```bash
docker-compose up -d
```

---

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `GROQ_API_KEY` | API key for Groq LLM service | Yes | - |
| `FLASK_DEBUG` | Enable Flask debug mode | No | `False` |
| `FLASK_PORT` | Port for Flask application | No | `5000` |

### LLM Model Selection

You can switch between different LLM models in `llm_call.py`:

- **gpt-oss-120b**: Large model with 120B parameters (default)
- **gpt-oss-20b**: Smaller, faster model with 20B parameters
- **qwen-32b**: Qwen3 model with 32B parameters
- **kimik2**: Kimi K2 Instruct model

To change the model, modify the function call in `agent.py`:

```python
# Current default
response = gpt_oss_120b(messages, tools=TOOL_SCHEMAS)

# Change to different model
response = qwen_32b(messages, tools=TOOL_SCHEMAS)
```

---

## 📖 Usage

### Web Interface

1. Open your browser to `http://localhost:5000`
2. Type your query in the input box
3. Press Enter or click "Send"
4. The agent will process your query and respond with the appropriate information

**Example Queries:**

- "What is the population of Tokyo?"
- "Search the web for the latest AI news"
- "Calculate 15% of 2500"
- "What time is it now?"
- "Tell me about quantum computing and find recent research papers"

### Command Line Interface

Run the CLI version:

```bash
python main.py
```

Then enter your queries when prompted. Type `exit` to quit.

---

## 🛠️ Available Tools

| Tool | Description | Example Use Case |
|------|-------------|------------------|
| **wikipedia_search** | Searches Wikipedia for information | "Tell me about Albert Einstein" |
| **web_search** | Performs DuckDuckGo web search | "Latest news about AI" |
| **web_scraper** | Scrapes and summarizes web pages | "Summarize information from tech blogs" |
| **calculator** | Evaluates mathematical expressions | "Calculate sqrt(144) + 25 * 3" |
| **current_time** | Returns current date and time | "What time is it?" |

### Tool Usage Examples

**Wikipedia Search**
```python
# Query: "Tell me about the Eiffel Tower"
# Tool Called: wikipedia_search(query="Eiffel Tower")
# Returns: Summary of Eiffel Tower from Wikipedia
```

**Web Search + Web Scraper**
```python
# Query: "Find and summarize the latest SpaceX news"
# Tools Called: 
#   1. web_search(query="latest SpaceX news")
#   2. web_scraper(query="[selected URL from search results]")
# Returns: Summarized content from the most relevant article
```

**Calculator**
```python
# Query: "Calculate the compound interest on $1000 at 5% for 3 years"
# Tool Called: calculator(expression="1000 * (1 + 0.05)**3")
# Returns: 1157.625
```

---

## 📡 API Reference

### REST API Endpoints

#### `POST /chat`

Send a message to the agent and receive a response.

**Request:**
```json
{
  "message": "What is the capital of France?"
}
```

**Response:**
```json
{
  "response": "The capital of France is Paris. It is located in the north-central part of the country..."
}
```

**Error Response:**
```json
{
  "error": "Error message here"
}
```

**Status Codes:**
- `200 OK`: Successful response
- `400 Bad Request`: Missing or invalid message
- `500 Internal Server Error`: Server-side error

---

## 📁 Project Structure

```
agentgo/
│
├── app.py                 # Flask web application
├── agent.py              # Main agent logic and tool orchestration
├── llm_call.py          # LLM API integration (Groq)
├── tools.py             # Tool implementations
├── main.py              # CLI entry point
├── index.html           # Web UI interface
│
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker container configuration
├── .env                # Environment variables (create this)
│
└── README.md           # This file
```

### File Descriptions

- **`app.py`**: Flask application that serves the web interface and handles HTTP requests
- **`agent.py`**: Core agent logic that manages tool selection and execution loop
- **`llm_call.py`**: Wrapper functions for different LLM models via Groq API
- **`tools.py`**: Implementation of all available tools (search, scraping, calculator, etc.)
- **`main.py`**: Command-line interface for terminal-based interaction
- **`index.html`**: Modern, responsive web interface with dark mode support

---

## 🔧 Advanced Configuration

### Custom Tool Creation

To add a new tool:

1. **Define the tool function in `tools.py`:**

```python
def my_custom_tool(param1: str, param2: int) -> str:
    """
    Description of what this tool does.
    """
    try:
        # Your tool implementation
        result = f"Processed {param1} with {param2}"
        return result
    except Exception as e:
        return f"Error: {str(e)}"
```

2. **Add the tool schema to `agent.py`:**

```python
{
    "type": "function",
    "function": {
        "name": "my_custom_tool",
        "description": "What this tool does",
        "parameters": {
            "type": "object",
            "properties": {
                "param1": {"type": "string"},
                "param2": {"type": "integer"}
            },
            "required": ["param1", "param2"]
        }
    }
}
```

3. **Register the tool in `TOOL_FUNCTIONS` dictionary:**

```python
TOOL_FUNCTIONS = {
    # ... existing tools
    "my_custom_tool": tools.my_custom_tool
}
```

### Adjusting Agent Behavior

You can modify agent behavior in `agent.py`:

- **Change max iterations**: Modify `max_iterations` variable (default: 15)
- **Customize system prompt**: Edit the system message in `run_agent()` function
- **Tool execution logging**: Add/remove print statements in the tool execution loop

---

## 🎯 Use Cases

### Research Assistant
```
Query: "Find information about renewable energy trends in 2024 and calculate 
the growth rate if solar adoption increased from 15% to 23%"

The agent will:
1. Use web_search to find recent renewable energy data
2. Use web_scraper to extract detailed information
3. Use calculator to compute the growth rate
4. Synthesize all information into a comprehensive response
```

### Educational Tool
```
Query: "Explain quantum entanglement and search for recent experimental results"

The agent will:
1. Use wikipedia_search to get foundational information
2. Use web_search to find recent research papers
3. Combine information into an educational response
```

### Data Analysis Helper
```
Query: "What's the current time and calculate how many hours until midnight"

The agent will:
1. Use current_time to get the current time
2. Use calculator to compute hours remaining
3. Provide the answer
```

---

## 🧪 Testing

### Running Tests

```bash
# Test individual tools
python tools.py

# Test the agent
python main.py
```

### Example Test Queries

1. **Simple calculation**: "What is 15% of 250?"
2. **Web search**: "Latest developments in quantum computing"
3. **Wikipedia query**: "Tell me about the Roman Empire"
4. **Complex query**: "Search for Python programming tutorials and calculate the time to learn basics if studying 2 hours daily for 30 days"
5. **Time query**: "What time is it now?"

---

## 🚢 Deployment

### Production Deployment Checklist

- [ ] Set `FLASK_DEBUG=False` in production
- [ ] Use a production WSGI server (Gunicorn, uWSGI)
- [ ] Set up HTTPS/SSL certificates
- [ ] Configure proper logging
- [ ] Set up monitoring and alerting
- [ ] Implement rate limiting
- [ ] Add authentication if needed
- [ ] Set up database for conversation history (optional)

### Example Production Setup with Gunicorn

1. **Install Gunicorn:**
   ```bash
   pip install gunicorn
   ```

2. **Create `gunicorn_config.py`:**
   ```python
   bind = "0.0.0.0:5000"
   workers = 4
   worker_class = "sync"
   timeout = 120
   accesslog = "-"
   errorlog = "-"
   loglevel = "info"
   ```

3. **Run with Gunicorn:**
   ```bash
   gunicorn -c gunicorn_config.py app:app
   ```

### Cloud Deployment Options

- **Heroku**: Use the included `Dockerfile` for container deployment
- **AWS ECS/EKS**: Deploy using Docker containers
- **Google Cloud Run**: Serverless container deployment
- **DigitalOcean App Platform**: Easy container deployment
- **Railway**: Simple git-based deployment

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Add docstrings to all functions
- Include error handling in tools
- Test your changes before submitting
- Update documentation for new features

---

## 🐛 Troubleshooting

### Common Issues

**Issue: "GROQ_API_KEY not found"**
- Solution: Make sure you've created a `.env` file with your API key

**Issue: "Module not found" errors**
- Solution: Ensure all dependencies are installed: `pip install -r requirements.txt`

**Issue: Web scraper returns errors**
- Solution: Some websites block scraping. Try a different URL or add headers to the request

**Issue: Calculator returns syntax error**
- Solution: Ensure mathematical expressions use Python syntax (e.g., `**` for exponents, not `^`)

**Issue: Port 5000 already in use**
- Solution: Change the port in `app.py` or kill the process using port 5000

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Groq** for providing fast LLM inference
- **LangChain** for LLM integration framework
- **Flask** for web framework
- **DuckDuckGo** for web search capabilities
- **Wikipedia** for knowledge base access
- All contributors who help improve this project

---

<div align="center">

**[⬆ back to top](#agentgo---intelligent-ai-agent-with-tool-integration)**

</div>
