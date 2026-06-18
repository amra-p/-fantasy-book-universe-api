from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# This is your first endpoint!
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Fantasy Book Universe API!"})

@app.route('/books')
def get_books():
    return jsonify({
        "books": [
            {"title": "Throne of Glass", "author": "Sarah J. Maas"},
            {"title": "A Court of Thorns and Roses", "author": "Sarah J. Maas"}
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)
    