import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "service": "Scraper-as-a-Service",
        "payment_network": "Polygon (USDT)"
    })

@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.json or {}
    target_url = data.get('url')
    
    if not target_url:
        return jsonify({"error": "Target URL is required"}), 400
        
    # Placeholder for payment verification & scraping trigger
    return jsonify({
        "message": "Payment address generated. Send USDT on Polygon to proceed.",
        "target": target_url,
        "amount_usdt": "5.00",
        "wallet": "0xYourPolygonWalletAddressHere"
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
