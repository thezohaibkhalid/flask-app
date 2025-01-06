from flask import Blueprint, render_template, request, jsonify
from services.scraper import scrape_google_maps
import math

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term']
    limit = int(request.form['limit'])
    
    results = scrape_google_maps(search_term, limit)
    print(results)
    
    return render_template('results.html', results=results, search_term=search_term, 
                           total_results=len(results), page=1, limit=10)

@search_bp.route('/page/<int:page>')
def get_page(page):
    search_term = request.args.get('search_term')
    limit = int(request.args.get('limit', 10))
    
    results = scrape_google_maps(search_term, limit)
    
    start = (page - 1) * 10
    end = start + 10
    page_results = results[start:end]
    
    return jsonify({
        'results': page_results,
        'total_pages': math.ceil(len(results) / 10)
    })