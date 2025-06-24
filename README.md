
# 🤖 Goal-Oriented Web Agent using LLaMA-3

An intelligent, interactive terminal-based agent that leverages **Large Language Models (LLMs)** and **web search tools** to accomplish **goal-driven information retrieval tasks**. This agent is powered by the **Agno Framework**, integrated with **SerpAPI** for real-time data, and designed for iterative reflection and human-in-the-loop improvement.

> A project that demonstrates the power of combining structured goal logic with LLM reasoning.

---

## 🧠 What It Does

- 🔍 **Searches the web** in real-time using SerpAPI
- 🧭 **Prioritizes and manages goals** based on urgency and context
- 🔁 **Reflects on failures** and adapts strategy intelligently
- 🗣️ **Interacts with the user** for feedback, clarification, and follow-up queries
- ✨ **Powered by LLaMA 3.3 70B** via Groq for high-quality, fast responses

---

## 🧰 Features

| Feature                     | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| 🎯 Goal-Driven Reasoning   | Define goals interactively and execute them with intelligent prioritization |
| 🔍 Real-Time Search        | Queries SerpAPI for latest information                                      |
| 🔁 Task Reflection         | Learns from failure and retries with adaptive strategies                    |
| 📊 Performance Tracking    | Tracks task attempts and failures for self-monitoring                       |
| 🧠 Clarification Loop      | Prompts the user for input if the response isn’t satisfactory               |
| 🗂️ Simple CLI Workflow     | Fully functional in terminal for rapid use and prototyping                  |

---

## 🛠️ Tech Stack

### 🔗 Backend
- **Python 3.x**
- **Agno Framework** — Agent architecture
- **Groq LLaMA-3.3 70B** — Large Language Model via API
- **SerpAPI** — Web search data source
- **dotenv** — API key management

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/agent-llama.git
cd agent-llama
```

### 2. Install Python Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Create `.env` File

```bash
touch .env
```

Add the following keys:

```
SERPAPI_API_KEY=your_serpapi_key_here
GROQ_PI_KEY=your_groq_key_here
```

---

## 🚀 Running the Agent

```bash
python goal_oriented_llama_agent.py
```

You’ll be prompted to:

1. Enter your first goal (e.g. “What is the GDP of India in 2024?”)
2. Review the response from the agent
3. Give feedback — is it satisfactory or not?
4. Add clarifications or continue to the next goal

---

## 🧪 Sample Queries to Try

- “Find recent news about India's space program”
- “Give me the latest stock prices for Tesla”
- “What are the top AI conferences in 2025?”
- “Find budget details for Union Budget 2025”

---

## 📦 Directory Structure

```
📁 agent-llama/
│
├── goal_oriented_llama_agent.py   # Main script with the agent logic
├── .env                           # Environment file for API keys
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

---

## 🔮 Future Enhancements

- [ ] Web UI with Streamlit or Flask
- [ ] Long-term memory using a vector database
- [ ] Plugin support for PDF summarization and email scraping
- [ ] Agent orchestration with multiple goals and sub-goals

---

## 📝 License

MIT License. Feel free to use, modify, and share.

---

## 👨‍💻 Authors

Built with ❤️ by:

- **Kaushal Borkar**  
- [Agno Framework](https://github.com/agnos-ai)
- [Groq LLaMA API](https://groq.com)
- [SerpAPI](https://serpapi.com)

---

## 📢 Acknowledgments

- OpenAI & Meta for LLaMA-3
- SerpAPI for real-time search results
- Groq for ultra-fast model inference
- The Agno community for agent framework

---

> "It’s not just a chatbot. It’s an agent that *thinks*, *reflects*, and *learns* from you."
