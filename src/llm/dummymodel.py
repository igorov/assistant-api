from .model import ModelInterface

class DummyModel(ModelInterface):
    def query(self, question, context):
        result = {
            "response": "Respuesta sin modelo",
            "product": "prueba"
        }
        return result