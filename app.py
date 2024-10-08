from flask import Flask

from rest.index import index_app

def create_app():
    app = Flask(__name__)
    app.register_blueprint(index_app)
    return app

def main():
    app = create_app()
    app.run(debug=True)
    
if __name__ == "__main__":
    main()