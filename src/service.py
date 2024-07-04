from llm.model import ModelInterface
from llm.dummymodel import DummyModel
from llm.llama3model import Llama3Model
from repository import save_document, get_documents

def get_answer(question, chromaObject):
    try:
        # Obtiene el contexto de la pregunta
        docs = chromaObject.get_context(question)
        
        # Instancia un objeto del modelo LLM
        model: ModelInterface = Llama3Model()
        result = model.query(question, docs)
        
        save_document(question, result['response'], result['product'])
    
        return result['response'], True
    except Exception as e:
        print(e)
        return "No se pudo obtener una respuesta", False

def get_questions():
    try:
        docs = get_documents()
        questions = []
        products = {
            #"nuevo": 33
        }
        for doc in docs:
            element = doc.to_dict()
            products[element['product']] = products.get(element['product'], 0) + 1
            questions.append(element)
        print(f"Cantidad de registros de la coleccion: {len(questions)}")
        return {
            "questions": questions,
            "products": products
        }
    except Exception as e:
        print(f"Excepcion e service: {e}")
        return []