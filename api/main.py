import json
import os
import requests

def handler(request):
    try:
        # Vercel ke liye request object se body lena
        body = request.json
        message = body.get('message', {})
        chat_id = message.get('chat', {}).get('id')
        user_text = message.get('text', '')

        # BOT_TOKEN ko environment variables se securely lena
        BOT_TOKEN = os.environ.get('BOT_TOKEN')
        TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        if not chat_id or not user_text:
            return "OK" # Telegram ko batana ki sab theek hai

        # User ko wahi message wapas bhejna (Echo Bot)
        response_text = f"Aapne bheja (Vercel se): {user_text}"

        payload = {
            'chat_id': chat_id,
            'text': response_text
        }

        requests.post(TELEGRAM_URL, json=payload)

        return "OK" # Hamesha 200 OK response bhejna

    except Exception as e:
        print(f"Error: {e}")
        return str(e) # Error bhejna
