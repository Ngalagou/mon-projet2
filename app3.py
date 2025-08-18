from flask import Flask
from anti_ddos import anti_ddos_middleware

app = Flask(__name__)  # ← Cette ligne doit venir avant toute utilisation de @app

@app.before_request
def before():
    anti_ddos_middleware()

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Page protégée</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #4facfe, #00f2fe);
                color: #fff;
                text-align: center;
                padding-top: 100px;
            }
            h1 {
                font-size: 3em;
                margin-bottom: 20px;
            }
            p {
                font-size: 1.2em;
            }
            .box {
                background-color: rgba(0, 0, 0, 0.3);
                padding: 30px;
                border-radius: 15px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 Bienvenue sur la page protégée !</h1>
            <p>Votre accès est sécurisé grâce à notre système anti-DDoS.</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
