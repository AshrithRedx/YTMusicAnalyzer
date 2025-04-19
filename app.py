from flask import Flask, request, jsonify, send_file
from fetch_playlist import get_playlist_data

app = Flask(__name__)

@app.route("/analyze", methods=["GET"])
def analyze_playlist():
    playlist_id = request.args.get("playlist_id")
    if not playlist_id:
        return jsonify({"error": "Missing playlist_id"}), 400

    try:
        data = get_playlist_data(playlist_id)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/plot", methods=["GET"])
def download_plot():
    return send_file("artist_frequency.png", mimetype="image/png")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

