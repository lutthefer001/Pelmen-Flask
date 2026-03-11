from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# TELEGRAM SOZLAMALARI
BOT_TOKEN = "BOT_TOKENINGIZNI_YOZING"
CHAT_ID = "ID_RAQAMINGIZNI_YOZING"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
    data = request.json
    product = data.get('product')
    price = data.get('price')
    pubg_id = data.get('pubg_id')

    message = f"🚀 *YANGI BUYURTMA*\n\n📦 *Mahsulot:* {product}\n💰 *Narxi:* {price}\n🆔 *PUBG ID:* {pubg_id}"
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return jsonify({"status": "success"})
        return jsonify({"status": "error", "msg": "Telegramga yuborilmadi"}), 500
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
