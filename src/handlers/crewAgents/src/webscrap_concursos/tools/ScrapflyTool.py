# src/webscrap_concursos/tools/ScrapflyTool.py
from crewai_tools import ScrapflyScrapeWebsiteTool
from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

from os import getenv
from dotenv import load_dotenv
load_dotenv()

class ScrapflyInput(BaseModel):
    url: str = Field(..., description="URL to scrape using Scrapfly")

class ScrapflyTool(BaseTool):
    name: str = "ScrapflyTool"
    description: str = (
        "Uses the Scrapfly API to scrape a given URL, returning the website content."
    )
    args_schema: Type[BaseModel] = ScrapflyInput

    def _run(self, url: str) -> str:
        """Run the Scrapfly scrape process."""
        api_key = getenv("SCRAPFLY_API_KEY")
        if not api_key:
            return "Error: SCRAPFLY_API_KEY not found in environment."

        try:
            scrape_tool = ScrapflyScrapeWebsiteTool(api_key=api_key)
            result = scrape_tool.run(url)
            return result
        except Exception as e:
            return f"Error scraping {url}: {e}"


