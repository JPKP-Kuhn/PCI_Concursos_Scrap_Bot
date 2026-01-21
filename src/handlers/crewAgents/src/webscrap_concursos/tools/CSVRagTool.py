from crewai_tools import CSVSearchTool
from typing import Type, Optional
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import json, os
from datetime import datetime

class CSVRagToolSchema(BaseModel):
    """Parâmetros para busca no CSV"""
    user_id: str = Field(..., description="ID do usuário (para localizar o arquivo CSV)")
    timestamp: str = Field(..., description="Data no formato DDMMYYYY usada no nome do arquivo CSV")
    query: Optional[str] = Field("", description="Texto opcional para buscar dentro do CSV (ex: cargo, órgão)")
    min_salary: Optional[float] = Field(None, description="Filtrar por salário mínimo desejado")
    today: Optional[str] = Field(default_factory=lambda: datetime.now().strftime("%d%m%Y"), description="Data atual para verificar inscrições abertas")

class CSVRagTool(BaseTool):
    name: str = "CSVRagTool"
    description: str = (
        "Busca e filtra dados no arquivo CSV de concursos públicos, "
        "utilizando a ferramenta nativa CSVSearchTool do CrewAI. "
        "Retorna resultados filtrados conforme critérios de pesquisa."
    )
    args_schema: Type[BaseModel] = CSVRagToolSchema

    def _run(self, user_id: str, timestamp: str, query: str = "", 
             min_salary: Optional[float] = None, today: Optional[str] = None) -> str:
        
        # Caminho esperado do CSV
        file_name = f"{user_id}_{timestamp}.csv"
        file_path = os.path.join("src", "handlers", "crewAgents", "knowledge", "users_csv", file_name)

        if not os.path.exists(file_path):
            return json.dumps({"error": f"Arquivo {file_name} não encontrado."}, ensure_ascii=False)

        try:
            # Usa a própria ferramenta nativa
            csv_tool = CSVSearchTool(csv_path=file_path)

            # Se o usuário quiser fazer uma query textual
            if query:
                raw_result = csv_tool.run(query)
            else:
                raw_result = csv_tool.run("listar concursos ativos e informações principais")

            # Opcionalmente, podemos cortar a saída para 10 linhas
            lines = raw_result.splitlines()
            limited = "\n".join(lines[:15])  # evita resposta muito longa

            return limited

        except Exception as e:
            return json.dumps({"error": str(e)}, ensure_ascii=False)

    async def _arun(self, **kwargs):
        return self._run(**kwargs)

