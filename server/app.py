from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

app.model = pickle.load(open('/data/rules.pkl', 'rb'))

@app.route("/")
def hello():
    return "HELLO WORLD"

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    input_songs = set(data.get('songs', []))
    
    recommendations = []
    for ant, consq, confid in app.model:
        if ant.issubset(input_songs):
            recommendations.extend(consq)
    
    response = {
        'songs': list(set(recommendations)),
        'version': '1.0.0',
        'model_date': '2025-01-11'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=52048)
