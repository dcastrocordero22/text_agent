
#Wrapper de capacidades
class TextTool:
    def __init__(self, agent):
        self.agent = agent

    def execute(self, action: str, params: dict):
        if action == "top_palabras":
            return self.agent.top_palabras(params.get("n", 5))

        if action == "frecuencia_palabra":
            return self.agent.frecuencia_palabra(
                params.get("palabra", "")
            )

        if action == "total_palabras":
            return self.agent.total_palabras()

        if action == "total_palabras_unicas":
            return self.agent.total_palabras_distintas()
        
        if action == "total_palabras_procesadas":
                    return self.agent.total_palabras_procesadas()
        
        raise ValueError(f"Acción no soportada: {action}")
