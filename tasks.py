from crewai import Task
from tools import tool
from agents import news_researcher, news_writer

# Research task (Fetching real news)
research_task = Task(
    description=(
        "Use Serper API to identify the latest breaking news on {topic}."
        "Extract key insights from the top search results."
        "Summarize the major developments concisely."
    ),
    expected_output="A summary of the top 3 breaking news articles on {topic}.",
    tools=[tool],  # Use Serper API
    agent=news_researcher,
)

# Writing task (Generating an AI-written article)
write_task = Task(
    description=(
        "Write a professional article based on the latest news from {topic}."
        "Ensure clarity, accuracy, and journalistic integrity."
        "Format the article properly in markdown."
    ),
    expected_output="A 4-paragraph AI-generated news article on {topic}.",
    tools=[tool],
    agent=news_writer,
    async_execution=False,
    output_file="new-blog-post.md"
)
