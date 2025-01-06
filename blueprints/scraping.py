from flask import Blueprint, request, send_file
from services.playwright_service import scrape_and_save_csv

scraping_bp = Blueprint('scraping', __name__)

@scraping_bp.route("/scrape", methods=["POST"])
def scrape():
    # Get form data
    business_name = request.form.get("name")
    search_limit = request.form.get("limit")
    search_limit = int(search_limit) if search_limit else 10  # Default to 10 if not provided

    # Call the scraper function
    output_file = scrape_and_save_csv(business_name, search_limit)

    # Send the generated CSV file as a downloadable response
    return send_file(output_file, as_attachment=True)
