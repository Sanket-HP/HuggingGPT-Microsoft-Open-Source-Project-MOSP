from flask import Flask, request, jsonify
from models.model import process_query

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.get_json()
    query = data.get('query')
    response = process_query(query)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
