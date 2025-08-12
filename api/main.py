from flask import Flask, request
import os
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handler():
    try:
        body = request.json
        message = body.get('message', {})
        chat_id = message.get('chat', {}).get('id')
        user_text = message.get('text', '')

        BOT_TOKEN = os.environ.get('BOT_TOKEN')
        TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        if not chat_id or not user_text:
            return "OK", 200

        response_text = f"Aapne bheja (Flask se): {user_text}"

        payload = {
            'chat_id': chat_id,
            'text': response_text
        }

        requests.post(TELEGRAM_URL, json=payload)

        return "OK", 200

    except Exception as e:
        print(f"Error: {e}")
        return "Error", 500
