# src/webscrap_concursos/tools.webscrap_tool.py
from crewai_tools import ScrapeWebsiteTool
from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class ConcursosScrapeInput(BaseModel):
    """ Esquema para a ferramenta"""
    region: str = Field(..., description="Região do Brasil, ex., 'sul', 'centrooeste'")
    state: str = Field(..., description="Nome completo do estado, ex., 'santa catarina', 'amazonas'")
    abbreviation: str = Field(..., description="Abreviação de duas letras, ex., 'SC', 'AM'")

class ConcursoScrapeTool(BaseTool):
    name: str = "ConcursoScrapeTool"
    description: str = (
        "Realiza o scrape do site PCI Concursos em busca de uma região e estado específicos"
            "Esta tool constroi a URL como 'https://www.pciconcursos.com.br/concursos/{region}/#{state_abbreviation}'"
            "Por fim ela retorna o conteúdo dessa página, que será útil para atender o {topic} do cliente"
    )
    args_schema: Type[BaseModel] = ConcursosScrapeInput

    def _run(self, region: str, state: str, abbreviation: str) -> str:
        base_url = f"https://www.pciconcursos.com.br/concursos/{region}/#{abbreviation}"
        scrapper = ScrapeWebsiteTool()
        print(10*'#')
        print(f"Scraping from URL: {base_url}")
        print(10*'#')
        try:
            content = scrapper.run(website_url=base_url)
            return f"Scraped data for {state} ({abbreviation}):\n\n{content[:1000]}"
        except Exception as e:
            return f"Error while scraping {base_url}: {e}"

