import logging
from crewai import Crew
from crewai.task import Task
from agents import ScraperAgent, SummarizerAgent, AnalystAgent

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class ResearchCrew:
    def __init__(self):
        logger.info("Initializing ResearchCrew...")

        # Instantiate agents
        self.scraper = ScraperAgent()
        self.summarizer = SummarizerAgent()
        self.analyst = AnalystAgent()

        logger.info("Agents initialized successfully.")

        # Define tasks for each agent
        self.scrape_task = Task(
            agent=self.scraper,
            description="Scrape the content from the given URL.",
            expected_output="Extracted text data from the webpage."
        )

        self.summarize_task = Task(
            agent=self.summarizer,
            description="Summarize the scraped content.",
            expected_output="A concise summary of the extracted text."
        )

        self.analyze_task = Task(
            agent=self.analyst,
            description="Extract key insights from the summary.",
            expected_output="Key insights derived from the summarized content."
        )

        logger.info("Tasks defined successfully.")

        # Create a Crew instance
        self.crew = Crew(
            agents=[self.scraper, self.summarizer, self.analyst],
            tasks=[self.scrape_task, self.summarize_task, self.analyze_task]
        )

        logger.info("Crew initialized successfully.")

    def process(self, url):
        logger.info(f"Processing URL: {url}")

        try:
            logger.info("Starting web scraping task...")
            scraped_content = self.scraper.process(url)
            logger.info("Web scraping completed.")

            logger.info("Starting summarization task...")
            summary = self.summarizer.process(scraped_content)
            logger.info("Summarization completed.")

            logger.info("Starting analysis task...")
            insights = self.analyst.process(summary)
            logger.info("Analysis completed.")

            logger.info("Processing completed successfully.")

            return {"summary": summary, "insights": insights}
        
        except Exception as e:
            logger.error(f"Error during processing: {e}", exc_info=True)
            return {"error": str(e)}
