import os
from flask import Flask, request, jsonify
from haystack import Document
from haystack.components.readers import ExtractiveReader

from logging_config import configure_logging


# CONFIGURE GPU
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


# CREATE APP
app = Flask(__name__)


# LOGGING CONFIGURATION
configure_logging(app)


# INITIALIZE READER
reader = ExtractiveReader(model="deepset/roberta-base-squad2")
reader.warm_up()


# ROUTES
@app.route('/query', methods=['POST'])
def query():
    # Get the question and context from the request
    data = request.json
    question = data.get('question')
    docs = [Document(content=data.get('context'))]

    if not question:
        return jsonify({'error': 'No question provided'}), 400
    
    if not docs[0].content:
        return jsonify({'error': 'No context provided'}), 400

    # Run the reader with the question and documents
    result = reader.run(query=question, documents=docs)

    # Extracting answers from the result
    answers = [{'answer': ans.data, 'score': ans.score} for ans in result['answers']]

    return jsonify({'answers': answers}), 200

if __name__ == '__main__':
    app.run(debug=False)
