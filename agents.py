import asyncio
import os
import streamlit as st
from dotenv import load_dotenv
from crewai import Agent
from tools import tool  # Import Serper API tool
from langchain_google_genai import ChatGoogleGenerativeAI
import json  # Import JSON module

# Load environment variables
load_dotenv()

# Ensure API keys are set
google_api_key = os.getenv("GOOGLE_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")

if not google_api_key:
    st.error("🚨 GOOGLE_API_KEY is not set! Please check your .env file.")
    st.stop()
if not serper_api_key:
    st.warning("⚠️ SERPER_API_KEY is missing! You may not get real-time news.")

# Ensure an event loop exists
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Initialize Google Gemini model
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        verbose=True,
        temperature=0.5,
        google_api_key=google_api_key
    )
except Exception as e:
    st.error(f"🚨 Failed to initialize ChatGoogleGenerativeAI: {e}")
    st.stop()

# Initialize Agents
news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover the latest breaking news on {topic}",
    verbose=True,
    memory=True,
    backstory="You're a top news analyst specializing in finding breaking stories.",
    tools=[tool] if tool else [],  # Use tool only if available
    llm=llm,
    allow_delegation=True
)

news_writer = Agent(
    role="Writer",
    goal="Write compelling news reports about {topic}",
    verbose=True,
    memory=True,
    backstory="You're a journalist known for turning breaking news into engaging articles.",
    tools=[tool] if tool else [],
    llm=llm,
    allow_delegation=False
)

# 🎯 Streamlit UI
st.title("📰 AI-Powered News Reporter")
st.write("Get the latest news articles instantly!")

# User input
topic = st.text_input("Enter a news topic:", "")

if st.button("Get Latest News"):
    if not topic:
        st.warning("⚠️ Please enter a topic.")
    else:
        with st.spinner("🔎 Fetching latest news..."):
            try:
                # Ensure the tool is initialized before running
                if tool:
                    search_results = tool.run(query=topic)  # ✅ Corrected function call
                else:
                    search_results = []

                # ✅ Debugging: Print the raw response
                st.subheader("🔍 Raw API Response")
                st.write(search_results)  # Show raw response to debug

                # ✅ Check if response is a string (error case)
                if isinstance(search_results, str):
                    st.error(f"❌ Serper API returned an error: {search_results}")
                    st.stop()

                # ✅ Check if response is a valid JSON object
                if isinstance(search_results, dict) and "organic" in search_results:
                    articles = search_results["organic"]  # Extract actual news articles
                elif isinstance(search_results, list):
                    articles = search_results
                else:
                    articles = []  # Handle unexpected API responses

                if not articles:
                    st.error("⚠️ No news found. Try another topic.")
                else:
                    st.subheader("📰 Latest News Articles")
                    for idx, article in enumerate(articles[:5]):  # Show top 5 results
                        if isinstance(article, dict) and "title" in article and "link" in article:
                            st.write(f"**{idx+1}. [{article['title']}]({article['link']})**")
                            st.write(f"🔹 {article.get('snippet', 'No description available.')}\n")
                        else:
                            st.write(f"**{idx+1}.** (Invalid article format)")

            except json.JSONDecodeError as e:
                st.error(f"❌ JSON Parsing Error: {e}")
            except Exception as e:
                st.error(f"❌ Error fetching news: {e}")
