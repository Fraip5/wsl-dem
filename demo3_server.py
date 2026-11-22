"""
Демонстрация 3: Flask веб-сервер в WSL
Сервер запускается в Linux, но доступен по localhost в Windows
"""

from flask import Flask, jsonify
import socket
import platform

# создание Flask приложение
app = Flask(__name__)

@app.route("/")
def hello():
    """Главная страница"""
    return """
    <html>
        <head>
            <title>WSL Demo</title>
            <style>
                body { 
                    font-family: Arial, sans-serif; 
                    max-width: 800px; 
                    margin: 50px auto; 
                    padding: 20px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                }
                h1 { text-align: center; }
                .info { 
                    background: rgba(255,255,255,0.1); 
                    padding: 20px; 
                    border-radius: 10px;
                    margin: 20px 0;
                }
            </style>
        </head>
        <body>
            <h1>🐧 Привет из WSL!</h1>
            <div class="info">
                <p><strong>Я работаю в Linux,</strong> но доступен по localhost в Windows.</p>
                <p><strong>Hostname:</strong> """ + socket.gethostname() + """</p>
                <p><strong>Платформа:</strong> """ + platform.system() + """</p>
                <p><strong>Версия Python:</strong> """ + platform.python_version() + """</p>
            </div>
            <p>Попробуй также: <a href="/api/info" style="color: #ffd700;">/api/info</a></p>
        </body>
    </html>
    """

@app.route("/api/info")
def api_info():
    """API endpoint с информацией о системе"""
    return jsonify({
        "message": "Привет из WSL!",
        "hostname": socket.gethostname(),
        "platform": platform.system(),
        "python_version": platform.python_version(),
        "working_directory": __file__
    })

if __name__ == "__main__":
    print("=" * 50)
    print("WSL Demo Server запущен!")
    print("=" * 50)
    print(f"Открой в браузере Windows: http://localhost:5000")
    print(f"API endpoint: http://localhost:5000/api/info")
    print("=" * 50)
    
    # Запускаем сервер на всех интерфейсах (важно для WSL!)
    app.run(host="0.0.0.0", port=5000, debug=True)
