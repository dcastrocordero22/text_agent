class Orchestrator:
    def __init__(self, tool):
        self.tool = tool

    def run(self, request):
        accion = request.get("accion")
        parametros = request.get("parametros", {})

        if not accion:
            raise ValueError("No se especificó ninguna acción")

        return self.tool.execute(accion, parametros)
