from flask import Flask
from anti_ddos import anti_ddos_middleware

app = Flask(__name__)

@app.before_request
def before():
    anti_ddos_middleware()

@app.route('/')
def index():
    return "Bienvenue sur la page protégée!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
