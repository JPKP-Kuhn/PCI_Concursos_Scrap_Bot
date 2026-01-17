from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# Tools are defined in tools/
from .tools.ConcursoScrapeTool import ConcursoScrapeTool
from .tools.ScrapflyTool import ScrapflyTool
from .tools.ReadUserPreferencesTool import file_read_tool

concurso_scrape_tool = ConcursoScrapeTool()
scrapfly_tool = ScrapflyTool()
read_preferences_tool = file_read_tool()

# Agents and Tasks are defined in config/agents.yaml and config/tasks.yaml
@CrewBase
class WebscrapConcursos():
    """WebscrapConcursos crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def context_planner_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['context_planner_agent'], # type: ignore[index]
            verbose=True,
            allow_delegation=False,
            memory=True,
            reasoning=True,
            tools=[read_preferences_tool],
            allow_code_executer=False,
            multimodal=False
        )

    @agent
    def webscrap_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['webscrap_agent'], # type: ignore[index]
            verbose=True,
            tools=[scrapfly_tool, concurso_scrape_tool],
            memory=False,
            allow_delegation=False,
            reasoning=False,
            allow_code_execution=False
        )

    @agent
    def data_analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['data_analysis_agent'], # type: ignore[index]
            verbose=True,
            allow_delegation=False,
            memory=True,
            reasoning=True,
            tools=[],
            allow_code_execution=False,
            multimodal=False
        )

    @agent
    def content_resume_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['content_resume_agent'], # type: ignore[index]
            verbose=True,
            allow_delegation=False,
            memory=True,
            reasoning=True,
            tools=[],
            allow_code_execution=False,
            multimodal=False
        )

    @agent
    def final_report_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['final_report_agent'], # type: ignore[index]
            verbose=True,
            allow_delegation=False,
            memory=True,
            reasoning=True,
            tools=[],
            allow_code_execution=False,
            multimodal=False
        )

    @task
    def content_planner_task(self) -> Task:
        return Task(
            config=self.tasks_config['context_planner_text'], # type: ignore[index]
            output_file='src/handlers/crewAgents/knowledge/output/content_planner.json'
        )

    @task
    def webscrap_task(self) -> Task:
        return Task(
            config=self.tasks_config['webscrap_task'], # type: ignore[index]
            output_file='src/handlers/crewAgents/knowledge/output/webscrap.md'
        )

    @task
    def data_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_analysis_task'], # type: ignore[index]
            output_file='src/handlers/crewAgents/knowledge/output/data_analysis.md'
        )

    @task
    def content_resume_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_resume_task'], # type: ignore[index]
            output_file='src/handlers/crewAgents/knowledge/output/content_resume.md'
        )

    @task
    def final_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['final_report_task'], # type: ignore[index]
            output_file='src/handlers/crewAgents/knowledge/output/final_report.md'
        )

    # Configures the crew
    @crew
    def crew(self) -> Crew:
        """Creates the WebscrapConcursos crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            memory=True
        )

