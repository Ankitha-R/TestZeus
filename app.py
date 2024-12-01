from flask import Flask, render_template, request, jsonify
import requests  # For sending requests to testzeus-hercules

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# API route to interact with testzeus-hercules
@app.route('/process', methods=['POST'])
def process():
    user_input = request.json.get('input')
    if not user_input:
        return jsonify({'error': 'No input provided'}), 400

    # Example interaction with testzeus-hercules (replace with actual API)
    try:
        # Mock response for testing
        response = {
            "input": user_input,
            "output": f"Processed: {user_input}"
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
