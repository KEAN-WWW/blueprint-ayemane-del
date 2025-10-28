from flask import Flask
from application.bp.homepage.routes import homepage

app = Flask(__name__)
app.register_blueprint(homepage)

if __name__ == '__main__':
    app.run(debug=True)
