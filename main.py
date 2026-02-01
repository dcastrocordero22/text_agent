from src.analyzer import TextAgent
from src.tools import TextTool
from src.orchestator import Orchestrator

if __name__ == "__main__":
    agent = TextAgent("data/input.csv")
    tool = TextTool(agent)
    orchestrator = Orchestrator(tool)

    request = {
        "accion": "top_palabras",
        "parametros": {
            "n": 5
        }
    }

    resultado = orchestrator.run(request)
    print(resultado)