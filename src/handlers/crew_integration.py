import sys, warnings
from datetime import datetime

from .crewAgents.src.webscrap_concursos.crew import WebscrapConcursos

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

class CrewaiIntegration:
    """ Integração entre crewai e chatbot """
    def __init__(self, username, topic, user_id):
        self.username = username
        self.topic = topic
        self.user_id = user_id
        # url for the webscrap
        self.url = "https://www.pciconcursos.com.br/"


    # inputs for crewai
    def _run(self):
        """
        Run the crew
        """
        inputs = {
            'user': self.username,
            'topic': self.topic,
            'url': self.url,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        try:
            result = WebscrapConcursos().crew().kickoff(inputs=inputs)
            return result
        except Exception as e:
            raise Exception(f"An error ocurred while running the crew: {e}")

    def _train(self):
        """
        Train the crew for a given number of iterations.
        """
        inputs = {
            'user': self.username,
            'topic': self.topic,
            'url': self.url
        }
        try:
            WebscrapConcursos().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

        except Exception as e:
            raise Exception(f"An error occurred while training the crew: {e}")

    def _replay(self):
        """
        Replay the crew execution from a specific task.
        """
        try:
            WebscrapConcursos().crew().replay(task_id=sys.argv[1])

        except Exception as e:
            raise Exception(f"An error occurred while replaying the crew: {e}")

    def _test(self):
        """
        Test the crew execution and returns the results.
        """
        inputs = {
            'user': self.username,
            'topic': self.topic,
            'url': self.url
        }

        try:
            WebscrapConcursos().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

        except Exception as e:
            raise Exception(f"An error occurred while testing the crew: {e}")

    def _run_with_trigger(self):
        """
        Run the crew with trigger payload.
        """
        import json

        if len(sys.argv) < 2:
            raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

        try:
            trigger_payload = json.loads(sys.argv[1])
        except json.JSONDecodeError:
            raise Exception("Invalid JSON payload provided as argument")

        inputs = {
            'user': self.username,
            'topic': self.topic,
            'url': self.url
        }

        try:
            result = WebscrapConcursos().crew().kickoff(inputs=inputs)
            return result
        except Exception as e:
            raise Exception(f"An error occurred while running the crew with trigger: {e}")
