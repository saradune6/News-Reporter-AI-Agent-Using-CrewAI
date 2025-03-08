### **📰 AI-Powered News Reporter**  
#### *An intelligent agent-based news research and reporting tool*  

![News Reporter AI](1.png)  

## **📌 Overview**  
This project is an **AI-powered news research and writing assistant** that fetches **real-time news** using **Serper API**, analyzes trends, and generates reports using **Google Gemini AI (via LangChain)**. It is built using **CrewAI**, allowing multiple AI agents to collaborate on researching and writing news articles dynamically.

---

## **📦 Features**  
✔️ **Fetches latest news** on any topic using **Serper API**  
✔️ **AI-generated summaries** using **Google Gemini (LangChain)**  
✔️ **Multi-agent collaboration** with **CrewAI**  
✔️ **Real-time search results** displayed in **Streamlit UI**  
✔️ **Easy-to-use web interface**  

---

## **🛠️ Tech Stack**  
- **Python 3.10+**  
- **Streamlit** (Frontend UI)  
- **CrewAI** (Multi-agent collaboration)  
- **LangChain** (LLM interaction)  
- **Google Gemini API** (AI-powered analysis)  
- **Serper API** (Live news search)  
- **dotenv** (Environment variable management)  

---

## **🚀 Installation & Setup**  
### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-username/AI-News-Reporter.git
cd AI-News-Reporter
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**  
```bash
python -m venv env
source env/bin/activate  # For macOS/Linux
env\Scripts\activate     # For Windows
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up API Keys**  
Create a `.env` file in the root directory and add your API keys:  
```bash
nano .env  # or use any text editor
```
Then add the following:  
```
SERPER_API_KEY=your_serper_api_key_here
GOOGLE_API_KEY=your_google_gemini_api_key_here
```
💡 **Tip:** You can get your API keys from:  
🔹 **Serper API** → [https://serper.dev/](https://serper.dev/)  
🔹 **Google AI Studio** (Gemini API) → [https://aistudio.google.com/](https://aistudio.google.com/)

### **5️⃣ Run the Application**  
```bash
streamlit run agents.py
```
The app will launch in your web browser. 🎉  

---

## **📸 Screenshots**  
### **🔍 Real-Time News Search**
![News Search Screenshot](https://user-images.githubusercontent.com/00000000/news-search.png)

### **✍️ AI-Generated News Reports**
![AI Report Screenshot](https://user-images.githubusercontent.com/00000000/ai-news-report.png)

---

## **📝 Project Structure**  
```
📂 AI-News-Reporter/
├── 📄 agents.py          # AI agents for news research and writing
├── 📄 crew.py            # CrewAI setup for multi-agent collaboration
├── 📄 tasks.py           # Tasks assigned to AI agents
├── 📄 tools.py           # Serper API integration
├── 📄 requirements.txt   # Dependencies
├── 📄 README.md          # Documentation
└── 📄 .env               # API keys (not included in the repo)
```

---

## **🔧 Troubleshooting**  
#### **❌ No news found?**  
👉 **Fix:** Ensure your `SERPER_API_KEY` is valid and check your usage limits on [Serper API Dashboard](https://serper.dev/).

#### **❌ Google Gemini API not working?**  
👉 **Fix:** Verify your `GOOGLE_API_KEY` is active and has sufficient quota.

#### **❌ JSON Parsing Error?**  
👉 **Fix:** Run `streamlit run agents.py`, then check the **"🔍 Raw API Response"** section to debug the API output.

---

## **📜 License**  
This project is licensed under the **MIT License**. Feel free to modify and use it as you like. ⭐

---

## **💡 Future Enhancements**  
✅ **Support for multiple news sources (Google News, Bing News, etc.)**  
✅ **AI-powered article summarization**  
✅ **Multilingual support for global news**  


🚀 **Built with AI, Powered by Innovation!** 📰🎯  

---

