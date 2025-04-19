from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Allow *all* origins temporarily (you can restrict it later)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/analyze", methods=["GET"])
def analyze_playlist():
    playlist_id = request.args.get("playlist_id")
    if not playlist_id:
        return jsonify({"error": "Missing playlist ID"}), 400
    try:
        data = get_playlist_data(playlist_id)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
