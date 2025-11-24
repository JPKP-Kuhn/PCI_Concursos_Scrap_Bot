from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from .tools.ConcursoScrapeTool import ConcursoScrapeTool
from .tools.ScrapflyTool import ScrapflyTool
concurso_scrape_tool = ConcursoScrapeTool()
scrapfly_tool = ScrapflyTool()

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class WebscrapConcursos():
    """WebscrapConcursos crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def context_planner_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['context_planner_agent'], # type: ignore[index]
            verbose=True,
            allow_delegation=False,
            memory=True,
            reasoning=True,
            tools=[],
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

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def content_planner_task(self) -> Task:
        return Task(
            config=self.tasks_config['context_planner_text'], # type: ignore[index]
            output_file='output/content_planner.json'
        )

    @task
    def webscrap_task(self) -> Task:
        return Task(
            config=self.tasks_config['webscrap_task'], # type: ignore[index]
            output_file='output/webscrap.md'
        )

    @task
    def data_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_analysis_task'], # type: ignore[index]
            output_file='output/data_analysis.md'
        )

    @task
    def content_resume_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_resume_task'], # type: ignore[index]
            output_file='output/content_resume.md'
        )

    @task
    def final_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['final_report_task'], # type: ignore[index]
            output_file='output/final_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the WebscrapConcursos crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            memory=True
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

