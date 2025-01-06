from flask import Flask, render_template
from blueprints.scraping import scraping_bp

app = Flask(__name__)

# Register the scraping blueprint
app.register_blueprint(scraping_bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
