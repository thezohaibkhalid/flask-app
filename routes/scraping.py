from flask import Blueprint, render_template, request, jsonify
from app.services.scraping_service import perform_scraping

scraping_bp = Blueprint('scraping', __name__, url_prefix="/")

@scraping_bp.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@scraping_bp.route("/scrape", methods=["POST"])
def scrape():
    search_term = request.json.get("search", "")
    total = request.json.get("total", 1)
    if not search_term:
        return jsonify({"error": "Search term is required"}), 400
    
    try:
        data = perform_scraping(search_term, total)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
