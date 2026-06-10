from flask import Flask
from routes.checkRoute import check_bp  
app = Flask(__name__)

app.register_blueprint(check_bp)
