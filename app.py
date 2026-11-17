from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/improve', methods=['POST'])
def improve():
    data = request.get_json()
    original_cv = data.get('cv_text', '')
    
    # For now, we will format/improve the CV text
    # (You can plug your AI/API call here later!)
    improved_cv = f"--- IMPROVED CV ---\n\n{original_cv}\n\n[Optimized for ATS and professional layout by CV Improver AI]"
    
    return jsonify({'improved_cv': improved_cv})

if __name__ == '__main__':
    app.run(debug=True)