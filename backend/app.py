from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from models.model import process_query

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.get_json()
    query = data.get('query')
    response = process_query(query)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
