from flask import Flask, request, render_template, send_file
from ..services.playwright_service import scrape_and_save_csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scrape", methods=["POST"])
def scrape():
    # Get form data
    business_name = request.form.get("name")
    search_limit = int(request.form.get("limit"))
    
    # Call the scraper function
    output_file = scrape_and_save_csv(business_name, search_limit)
    
    # Send the generated CSV file as a downloadable response
    return send_file(output_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
