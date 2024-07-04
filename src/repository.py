from google.cloud import firestore
import os

gcp_project = os.getenv('PROJECT_ID', 'is-tech-academy')
db_name = os.getenv('DB_NAME', 'tec-db')
collection_name = os.getenv('COLLECTION_NAME', 'questions')

db = firestore.Client(project=gcp_project, database=db_name)

def save_document(query, response, product):
    try:
        _, doc_ref = db.collection(collection_name).add({
            "query": query, 
            "response": response, 
            "product": product, 
            "date": firestore.SERVER_TIMESTAMP
        })
        print(f"Documento guardado con ID: {doc_ref.id}")
    except Exception as e:
        print(e)

def get_documents():
    try:
        docs = db.collection(collection_name).stream()
        return docs
    except Exception as e:
        print(f"Excepcion e repository: {e}")