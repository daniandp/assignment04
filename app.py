from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    # # read the APP_MESSAGE environment variable
    return os.getenv('APP_MESSAGE', 'No APP_MESSAGE set'), 200

@app.route('/health')
def health():
    # read the APP_HEALTH environment variable
    return os.getenv('APP_HEALTH', 'No APP_HEALTH set'), 200

if __name__ == '__main__':
    # default port 8085 for matching with docker-compose / Dockerfile
    port = int(os.getenv('PORT', 8085))
    app.run(host='0.0.0.0', port=port, debug=False)