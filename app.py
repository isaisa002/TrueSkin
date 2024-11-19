from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

products = [
    {
        "id": 1,
        "brand": "SKINRX004",
        "name": "Madagascar Centella Ampoule",
        "price": 19.99,
        "description": "Vegan and cruelty-free ampoule that contains 7 ingredients.",
        "categories": ["new_grade", "fungal_acne_safe", "reef_safe"],
        "image": "/static/images/1.jpg",
        "benefits": [
            "Helps calm and soothe sensitive skin",
            "Provides deep hydration",
            "Strengthens skin barrier",
            "Safe for fungal acne-prone skin"
        ]
    },
    {
        "id": 2,
        "brand": "PURITO",
        "name": "Oat-In Calming Gel Cream",
        "price": 16.99,
        "description": "Gentle moisturizer suitable for sensitive skin",
        "categories": ["hydrating", "sensitive_skin_safe"],
        "image": "/static/images/oat.jpg",
        "benefits": [
            "Gentle and non-irritating formula",
            "Suitable for sensitive skin",
            "Provides lasting hydration",
            "Contains soothing oat extract"
        ]
    },
      {
        "id": 5,
        "brand": "BEAUTY OF JOSEON",
        "name": "Glow Serum",
        "price": 17.99,
        "description": "Propolis and niacinamide brightening serum",
        "categories": ["hydrating", "new_grade"],
        "image": "/static/images/4.jpg",
        "benefits": [
            "Brightens skin tone",
            "Improves skin texture",
            "Anti-inflammatory properties",
            "Enhances natural glow"
        ]
    },
      {
        "id": 5,
        "brand": "BEAUTY OF JOSEON",
        "name": "Glow Serum",
        "price": 17.99,
        "description": "Propolis and niacinamide brightening serum",
        "categories": ["hydrating", "new_grade"],
        "image": "/static/images/6.jpg",
        "benefits": [
            "Brightens skin tone",
            "Improves skin texture",
            "Anti-inflammatory properties",
            "Enhances natural glow"
        ]
    },
      {
        "id": 5,
        "brand": "BEAUTY OF JOSEON",
        "name": "Glow Serum",
        "price": 17.99,
        "description": "Propolis and niacinamide brightening serum",
        "categories": ["hydrating", "new_grade"],
        "image": "/static/images/7.jpg",
        "benefits": [
            "Brightens skin tone",
            "Improves skin texture",
            "Anti-inflammatory properties",
            "Enhances natural glow"
        ]
    },
    {
        "id": 3,
        "brand": "COSRX",
        "name": "Advanced Snail 96 Mucin Power Essence",
        "price": 19.99,
        "description": "Hydrating essence with snail secretion filtrate",
        "categories": ["oil_control", "trending"],
        "image": "/static/images/8.jpg",
        "benefits": [
            "Intensive hydration",
            "Helps repair skin barrier",
            "Improves skin elasticity",
            "Soothes irritated skin"
        ]
    },
    {
        "id": 4,
        "brand": "ISNTREE",
        "name": "Green Tea Fresh Emulsion",
        "price": 22.99,
        "description": "Light moisturizer for oily skin types",
        "categories": ["oil_control", "trending"],
        "image": "/static/images/3.jpg",
        "benefits": [
            "Controls excess sebum",
            "Lightweight formula",
            "Antioxidant protection",
            "Mattifying effect"
        ]
    },
    {
        "id": 5,
        "brand": "BEAUTY OF JOSEON",
        "name": "Glow Serum",
        "price": 17.99,
        "description": "Propolis and niacinamide brightening serum",
        "categories": ["hydrating", "new_grade"],
        "image": "/static/images/4.jpg",
        "benefits": [
            "Brightens skin tone",
            "Improves skin texture",
            "Anti-inflammatory properties",
            "Enhances natural glow"
        ]
    },
    {
        "id": 6,
        "brand": "BENTON",
        "name": "Aloe BHA Skin Toner",
        "price": 17.99,
        "description": "Gentle exfoliating toner with aloe",
        "categories": ["oil_control", "soothing"],
        "image": "/static/images/5.jpg",
        "benefits": [
            "Gentle exfoliation",
            "Soothes irritated skin",
            "Hydrating properties",
            "Improves skin texture"
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/api/products')
def get_products():
    filter_type = request.args.get('filter', 'all')
    search_query = request.args.get('search', '').lower()
    
    filtered_products = products
    
    if filter_type != 'all':
        filtered_products = [p for p in products if filter_type in p['categories']]
    
    if search_query:
        filtered_products = [p for p in filtered_products 
                           if search_query in p['name'].lower() or 
                              search_query in p['brand'].lower() or 
                              search_query in p['description'].lower()]
    
    return jsonify(filtered_products)

if __name__ == '__main__':
    app.run(debug=True)