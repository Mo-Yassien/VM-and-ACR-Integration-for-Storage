import json
import os
from flask import Flask

app = Flask(__name__)

CONFIG_PATH = '/app/config.json'

@app.route('/')
def index():
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, 'r') as f:
                config_data = json.load(f)
            return f"Welcome to KKE Azure Labs: {config_data}\n"
        except Exception as e:
            return f"Error reading config: {str(e)}\n", 500
    else:
        return "Config file not found!\n", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)