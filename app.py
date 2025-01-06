from flask import Flask
from blueprints.main import main_bp
from blueprints.search import search_bp


def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(main_bp)
    app.register_blueprint(search_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)