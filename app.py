from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/trending')
def trending():
    # Placeholder response
    return jsonify({
        "status": "success",
        "data": [
            {"title": "Example Article 1", "source": "Twitter", "engagement": 1200},
            {"title": "Example Article 2", "source": "Reddit", "engagement": 950}
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)
