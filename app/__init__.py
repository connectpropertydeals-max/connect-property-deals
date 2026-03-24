from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "<h1>Connect Property Deals is LIVE 🚀</h1>"

    return app
