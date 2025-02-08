# ResearchCrew by NxtAI

ResearchCrew is an AI-powered research automation tool that utilizes Azure OpenAI and CrewAI to scrape, summarize, and analyze web content efficiently.

## 🚀 Features
- **Web Scraping**: Extracts relevant data from web pages.
- **Text Summarization**: Condenses large amounts of text into meaningful summaries.
- **Data Analysis**: Identifies key insights from summarized content.

## 📦 Tech Stack
- **FastAPI** for API development
- **CrewAI** for agent-based task management
- **Azure OpenAI** for AI-powered summarization & analysis

---

## 🛠️ Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.10+
- pip (Python package manager)
- An Azure OpenAI account with API keys

### Clone the Repository
```sh
 git clone https://github.com/NxtAI/ResearchCrew.git
 cd ResearchCrew
```

### Create a Virtual Environment (Optional but Recommended)
```sh
 python -m venv venv
 source venv/bin/activate   # On macOS/Linux
 venv\Scripts\activate      # On Windows
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

---

## 🔑 Configuration

### Set Up Environment Variables
Create a `.env` file in the root directory and add your Azure OpenAI credentials:
```ini
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_API_BASE=https://your-azure-instance.openai.azure.com
AZURE_OPENAI_API_VERSION=turbo-2024-04-09
```

---

## 🚀 Running the Application

### Start FastAPI Server
```sh
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### API Endpoint
- **Analyze a URL:** `GET /analyze?url=<your_url>`

Example:
```sh
curl "http://127.0.0.1:8000/analyze?url=https://example.com"
```



## 🤝 Contributing
We welcome contributions! Follow these steps:

1. **Fork** the repository.
2. **Clone** your forked repo:
   ```sh
   git clone https://github.com/your-username/ResearchCrew.git
   ```
3. **Create a feature branch**:
   ```sh
   git checkout -b feature-branch
   ```
4. **Make changes** and commit:
   ```sh
   git commit -m "Your commit message"
   ```
5. **Push changes** to your fork:
   ```sh
   git push origin feature-branch
   ```
6. **Open a Pull Request** on GitHub.

---

## 📝 License
This project is licensed under the MIT License.

---

## 📢 Contributors
We appreciate all contributors! Feel free to submit issues and pull requests to improve ResearchCrew. 😊

