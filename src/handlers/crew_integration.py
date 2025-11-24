import sys, warnings

from .crewAgents.src.webscrap_concursos.crew import WebscrapConcursos

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

class CrewaiIntegration:
    """ Integração entre crewai e chatbot """
    def __init__(self, username, topic):
        self.username = username
        self.topic = topic
        self.url = "https://www.pciconcursos.com.br/"


    def _run(self):
        inputs = {
            'user': self.username,
            'topic': self.topic,
            'url': self.url
        }
        try:
            result = WebscrapConcursos().crew().kickoff(inputs=inputs)
            return result
        except Exception as e:
            raise Exception(f"An error ocurred while running the crew: {e}")
