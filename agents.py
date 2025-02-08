import os
import logging
from openai import AzureOpenAI
from crewai import Agent

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),  # Use the latest Azure OpenAI API version
    azure_endpoint=os.getenv("AZURE_OPENAI_API_BASE")  # Set your Azure OpenAI endpoint
)

class ScraperAgent(Agent):
    def __init__(self):
        logger.info("Initializing ScraperAgent...")
        super().__init__(
            role="Web Scraper",
            goal="Extract relevant data from web pages efficiently.",
            backstory="An expert in web scraping, skilled in handling various data formats."
        )
        logger.info("ScraperAgent initialized successfully.")

    def process(self, url):
        logger.info(f"ScraperAgent processing URL: {url}")
        try:
            # Simulate scraping (replace this with actual scraping logic)
            content = f"Mocked content from {url}"
            logger.info("Scraping completed successfully.")
            return content
        except Exception as e:
            logger.error(f"Error during scraping: {e}", exc_info=True)
            return None

class SummarizerAgent(Agent):
    def __init__(self):
        logger.info("Initializing SummarizerAgent...")
        super().__init__(
            role="Text Summarizer",
            goal="Condense large amounts of text into meaningful summaries.",
            backstory="A linguistics expert trained in natural language processing and summarization."
        )
        logger.info("SummarizerAgent initialized successfully.")

    def process(self, content):
        logger.info("SummarizerAgent processing content...")
        try:
            response = client.chat.completions.create(
                model="gpt-4",  # Use your Azure OpenAI deployment name
                messages=[
                    {"role": "system", "content": "Summarize this content:"},
                    {"role": "user", "content": content}
                ]
            )
            summary = response.choices[0].message.content
            logger.info("Summarization completed successfully.")
            return summary
        except Exception as e:
            logger.error(f"Error during summarization: {e}", exc_info=True)
            return None

class AnalystAgent(Agent):
    def __init__(self):
        logger.info("Initializing AnalystAgent...")
        super().__init__(
            role="Data Analyst",
            goal="Identify key insights from summarized content.",
            backstory="A skilled researcher with experience in extracting trends and patterns from text data."
        )
        logger.info("AnalystAgent initialized successfully.")

    def process(self, summary):
        logger.info("AnalystAgent analyzing summary...")
        try:
            response = client.chat.completions.create(
                model="gpt-4",  # Use your Azure OpenAI deployment name
                messages=[
                    {"role": "system", "content": "Extract key insights from this:"},
                    {"role": "user", "content": summary}
                ]
            )
            insights = response.choices[0].message.content
            logger.info("Analysis completed successfully.")
            return insights
        except Exception as e:
            logger.error(f"Error during analysis: {e}", exc_info=True)
            return None
