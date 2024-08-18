import os
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import json

from .model import ModelInterface

class Llama3Model(ModelInterface):
    def query(self, question, context):
        model_name = os.getenv('MODEL_NAME', 'Asistente IS')

        model = ChatNVIDIA(model="meta/llama3-70b-instruct", temperature=0)
        template = """
        Responde a la pregunta basándote en el contexto que está delimitado por 5 asteriscos al inicio y al final.

        *****
        {context}
        *****

        Tu respuesta debe tener la siguiente estructura JSON con los siguientes campos:
        - response: Que contendrá la respuesta a la pregunta.
        - product: Debes identificar de que producto se trata la pregunta, pueden ser los siguientes valores:
            * seguro vehicular
            * seguro de viaje
            * seguro vida free
            * seguro universitario
            * seguro de vida con devolución
            * seguro rumbo
            * general: en caso de que no se pueda identificar el producto.

        Ante cualquier saludo o despedida, tu nombre es '{name}', y el 'product' será 'general'.
        La pregunta que debes responder es la siguiente:
        Pregunta: {question}
        """

        prompt = ChatPromptTemplate.from_template(template)
        rag_chain = (
            {
                "context": itemgetter("context"),
                "question": itemgetter("question"),
                "name": itemgetter("name")
            }
            | prompt
            | model
            | StrOutputParser()
        )

        response = rag_chain.invoke({"question": question, "context": context, "name": model_name})
        print("fin")
        # pasar de string json a objeto json
        result = json.loads(response)
        print(result)
        return result