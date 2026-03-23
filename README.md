# Terminal AI Chatbot (Streaming Enabled)

A **production-ready terminal-based AI chatbot** built with Python, featuring **streaming responses, token tracking, memory management, and modular architecture**.

---

## Features

- **Streaming AI Responses** – AI answers appear in real-time as they are generated.  
- **Mock Responses** – Automatically fallback when API key is missing or quota exceeded.  
- **Conversation Management** – `/clear` command to reset conversation.
- **History** - `/history` command to check history of the conversation. 
- **Token Tracking** – Tracks total tokens in conversation; warns when exceeding thresholds.  
- **Logging** – Conversation logs are saved daily in JSON format for review/debugging.  
- **Automated Tests** – Ensures token counting and conversation trimming work as expected.

---

## Project Structure
```
terminal-ai-chatbot/
│
├── src/
│ ├── main.py # Entry point
│ │
│ ├── core/
│ │ ├── chat.py # Streaming + API logic
│ │ ├── prompts.py # System prompt
│ │
│ ├── services/
│ │ ├── token_service.py # Token counting
│ │ ├── memory_service.py # Conversation trimming
│ │
│ ├── utils/
│ ├── logger.py # Logging system
│
├── logs/ # Generated logs (ignored in Git)
├── .env # API key (not committed)
├── requirements.txt
├── README.md
├── .gitignore
```


---

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/jyothsnapal29/terminal-ai-chatbot.git

cd terminal-ai-chatbot

---

### 2. Create virtual environment
python3 -m venv ai-env
source ai-env/bin/activate


---

### 3. Install dependencies
pip install -r requirements.txt


---

### 4. Add OpenAI API key (optional)
Create `.env` file:
OPENAI_API_KEY=your_api_key_here

If not provided, chatbot runs in **mock mode**

---

### 5. Run the chatbot

```python src/main.py```

Commands
---
/clear – Reset conversation history.

/history - Returns latest conversation history.

Exit or Quit – End session.

The chatbot will fallback to mock responses if the API fails or quota is exceeded.


Testing
---

Automated tests are included using pytest:

Token counting – validates count_tokens function.
Conversation trimming – validates trim_conversation_history function.

Run tests:
```cd src
pytest tests/
```
All tests should pass before committing changes.

## Example

You: What is AI?
Chatbot: AI (Artificial Intelligence) refers to systems that simulate human intelligence...

You: /clear

Chatbot: Conversation history cleared.


## Mock Mode Example (No API / Quota Exceeded)

You: What is AI?

Chatbot: [Mock] You said: 'What is AI?' | Total messages: 2


## 🐳 Run with Docker

### Build the image
docker build -t terminal-ai-chatbot .

### Run the container
docker run -it --rm terminal-ai-chatbot

### Run with environment variables
docker run -it --rm --env-file .env terminal-ai-chatbot


---

## Key Concepts Demonstrated

- LLM API integration (OpenAI)
- Streaming responses
- Tokenization (`tiktoken`)
- Context window management
- CLI-based UX design
- Error handling and fallback systems
- Modular Python architecture
- Basic unit test

---

## Future Improvements

- Add FastAPI backend
- Build React frontend
- Add chat history UI
- Integrate vector database (RAG)
- Support file uploads (PDF chat)

---

## License

MIT License

---

## Author

**Jyothsna Pal**

Aspiring AI Engineer | GenAI Developer | Building real-world AI systems





