from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from data import public_figures  # Updated to use category + name

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    name = request.form['name'].strip().lower()
    category = request.form['category'].strip().lower()

    # Check if the category exists
    if category not in public_figures:
        return jsonify({
            'error': f'Category "{category}" not found. Please select a valid category.'
        }), 404

    # Check if the name exists under that category
    if name not in public_figures[category]:
        return jsonify({
            'error': f'"{name.title()}" not found under "{category.title()}".'
        }), 404

    data = public_figures[category][name]

    total_score = round(
        (data['credibility'] * 0.4 + data['longevity'] * 0.3 + data['engagement'] * 0.3), 1
    )

    return jsonify({
        'name': name.title(),
        'country': data['country'],
        'credibility': data['credibility'],
        'longevity': data['longevity'],
        'engagement': data['engagement'],
        'total_score': total_score
    })

if __name__ == '__main__':
    app.run(debug=True)
