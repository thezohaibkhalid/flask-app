from flask import Blueprint, render_template, request, jsonify, send_from_directory
from services.scraper import scrape_google_maps
import math
import os
search_bp = Blueprint('search', __name__)
@search_bp.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term']
    limit = int(request.form['limit'])
    
    results = scrape_google_maps(search_term, limit)
 
    
    return render_template('index.html', csv_available=True)

