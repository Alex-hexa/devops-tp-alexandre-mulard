import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

IS_DEBUG = os.environ.get("FLASK_DEBUG", "0") == "1"
app.config["DEBUG"] = IS_DEBUG

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if SUPABASE_URL and SUPABASE_KEY:
    supabase_client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
else:
    supabase_client = None


@app.route("/api/cards", methods=["GET"])
def get_cards():
    if not supabase_client:
        return jsonify({"error": "Base de données non configurée"}), 500
    try:
        response = (
            supabase_client.table("cards")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )
        return jsonify(response.data)
    except Exception as e:
        return jsonify({"error": str(e) if IS_DEBUG else "Erreur serveur"}), 500


@app.route("/api/cards", methods=["POST"])
def add_card():
    if not supabase_client:
        return jsonify({"error": "Base de données non configurée"}), 500

    data = request.json
    if not data.get("name") or not data.get("code"):
        return jsonify({"error": "Nom et code requis."}), 400

    try:
        response = (
            supabase_client.table("cards")
            .insert({"name": data["name"], "code": data["code"]})
            .execute()
        )
        return jsonify(response.data), 201
    except Exception as e:
        return jsonify({"error": str(e) if IS_DEBUG else "Erreur serveur"}), 500


if __name__ == "__main__":
    app.run()
