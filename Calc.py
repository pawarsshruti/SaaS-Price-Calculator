from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# SaaS pricing tiers
tiers = {
    "basic": {"price": 10, "users": 5, "storage": 10},
    "pro": {"price": 20, "users": 10, "storage": 50},
    "enterprise": {"price": 50, "users": 100, "storage": 500}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    tier = data['tier']
    extra_users = max(0, int(data['users']) - tiers[tier]['users'])
    extra_storage = max(0, int(data['storage']) - tiers[tier]['storage'])
    
    base_price = tiers[tier]['price']
    user_price = extra_users * 2  # $2 per extra user
    storage_price = extra_storage * 0.1  # $0.1 per extra GB
    
    total_price = base_price + user_price + storage_price
    
    return jsonify({
        "base_price": base_price,
        "user_price": user_price,
        "storage_price": storage_price,
        "total_price": total_price
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
