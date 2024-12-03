from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with the actual TestZeus Hercules API URL
HERCULES_API_BASE = "https://api.testzeus-hercules.com/api"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query_hercules():
    data = request.form.get('data')
    try:
        response = requests.post(f"{HERCULES_API_BASE}/query", json={"data": data})
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
