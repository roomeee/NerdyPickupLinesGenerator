from flask import Flask, render_template
import json
import random

app = Flask(__name__)

def get_pickup_lines():
    with open('nerdy_pickup_lines.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data.get('nerdy_pickup_lines', [])


@app.route('/')
def index():
    pickup_line = random.choice(get_pickup_lines())
    return render_template('index.html', pickup_line=pickup_line)

if __name__ == '__main__':
    app.run(debug=True)
