from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Minha Aplicação Docker</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f0f0f0;
            }}
            .container {{
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #2c3e50;
            }}
            .info {{
                background-color: #3498db;
                color: white;
                padding: 15px;
                border-radius: 5px;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🐳 Aplicação Docker Funcionando!</h1>
            <p>Parabéns! Sua aplicação está rodando com sucesso no Docker.</p>
            <div class="info">
                <strong>Nome do Container:</strong> {hostname}
            </div>
            <p style="margin-top: 20px;">
                ✅ Dockerfile criado<br>
                ✅ Imagem Docker construída<br>
                ✅ Container executando<br>
                ✅ Mapeamento de portas configurado<br>
                ✅ Acessível pelo navegador
            </p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)