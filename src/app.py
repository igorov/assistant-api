from flask import Flask , request , jsonify
from flask_cors import CORS
import service
from chromais import ChromaDB


app = Flask(__name__)
CORS(app)

chromaObject = ChromaDB()

@app.route('/api/model' , methods=['POST'])
def get_answer():
    body = request.get_json()
    question = body['question']
    response, result = service.get_answer(question, chromaObject)
    if result:
        return jsonify({"response": response, "status": "OK"})
    else:
        return jsonify({"response": response, "status": "ERROR"})

@app.route('/api/questions' , methods=['GET'])
def get_questions():
    response = service.get_questions()
    return jsonify(response)

if __name__ == '__main__' :
    #app.run(debug=True)
    app.run(host='0.0.0.0', debug=True, port=8080)