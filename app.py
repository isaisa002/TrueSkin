from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

products = [
    {
        "id": 1,
        "brand": "SKINRX004",
        "name": "Madagascar Centella Ampoule",
        "price": 19.99,
        "description": "Vegan and cruelty-free ampoule that contains 7 ingredients.",
        "categories": ["new_grade", "fungal_acne_safe", "reef_safe"],
        "image": "/static/images/oat.jpg",
        "benefits": [
            "Helps calm and soothe sensitive skin",
            "Provides deep hydration",
            "Strengthens skin barrier",
            "Safe for fungal acne-prone skin"
        ],
        "ingredients": [
            "Centella Asiatica Extract",
            "Butylene Glycol",
            "Betaine",
            "Sodium Hyaluronate"
        ],
        "reviews": [
            {"name": "Anna", "rating": 5, "comment": "I recently added a centella serum to my skincare routine, and it’s been a game-changer for my sensitive skin."},
            {"name": "Dr. Rachel Ho ✅", "rating": 5, "comment": "Excellent for calming sensitive, acne-prone skin. Works well as a hydrating serum to strengthen the skin barrier and reduce inflammation effectively."}
        ],
        "transparency": 4
    },
    {
        "id": 2,
        "brand": "PURITO",
        "name": "Oat-In Calming Gel Cream",
        "price": 16.99,
        "description": "Gentle moisturizer suitable for sensitive skin",
        "categories": ["hydrating", "sensitive_skin_safe"],
        "image": "/static/images/1.jpg",
        "benefits": [
            "Gentle and non-irritating formula",
            "Suitable for sensitive skin",
            "Provides lasting hydration",
            "Contains soothing oat extract"
        ],
        "ingredients": [
            "Avena Sativa (Oat) Kernel Extract",
            "Panthenol",
            "Squalane",
            "Madecassoside"
        ],
        "reviews": [
            {"name": "Dr. Dray ✅", "rating": 5, "comment": "Formulated with soothing oat extract. Ideal for dry, irritated skin needing hydration. Lightweight texture makes it perfect for sensitive skin types."}
        ],
        "transparency": 3
    },
    {
        "id": 3,
        "brand": "COSRX",
        "name": "Advanced Snail 96 Mucin Power Essence",
        "price": 19.99,
        "description": "Hydrating essence with snail secretion filtrate",
        "categories": ["oil_control", "trending"],
        "image": "/static/images/2.jpg",
        "benefits": [
            "Intensive hydration",
            "Helps repair skin barrier",
            "Improves skin elasticity",
            "Soothes irritated skin"
        ],
        "ingredients": [
            "Snail Secretion Filtrate",
            "Sodium Hyaluronate",
            "Arginine",
            "Allantoin"
        ],
        "reviews": [
            {"name": "Dr. Dray ✅", "rating": 5, "comment": "Contains high levels of snail mucin for hydration, repair, and anti-aging benefits. Perfect for dry and dull skin."}
        ],
        "transparency": 4
    },
    {
        "id": 4,
        "brand": "Anua",
        "name": "Heartleaf 77% Soothing Toner",
        "price": 19.99,
        "description": "Calming and hydrating toner with 77% Heartleaf extract for sensitive skin",
        "categories": ["hydration", "soothing", "trending"],
        "image": "/static/images/3.jpg",
        "benefits": [
            "Calms redness and irritation",
            "Hydrates and soothes skin",
            "Non-sticky, lightweight texture",
            "Supports skin's natural barrier"
        ],
        "ingredients": [
            "Houttuynia Cordata Extract",
            "Butylene Glycol",
            "Glycerin",
            "1,2-Hexanediol"
        ],
        "reviews": [
            {"name": "Dr. Rachel Ho ✅", "rating": 5, "comment": "Heartleaf extract is excellent for calming inflammation and redness. Ideal for sensitive skin needing hydration and a non-sticky finish."}
        ],
        "transparency": 4
    },
    {
        "id": 5,
        "brand": "The Ordinary",
        "name": "Niacinamide 10% + Zinc 1%",
        "price": 12.50,
        "description": "High-strength vitamin and mineral formula to reduce the appearance of blemishes and congestion",
        "categories": ["oil_control", "brightening", "trending"],
        "image": "/static/images/4.jpg",
        "benefits": [
            "Regulates sebum production",
            "Minimizes appearance of pores",
            "Reduces redness and blemishes",
            "Brightens skin tone"
        ],
        "ingredients": [
            "Niacinamide",
            "Zinc PCA",
            "Pentylene Glycol",
            "Tamarindus Indica Seed Gum"
        ],
        "reviews": [
            {"name": "Dr. Rachel Ho ✅", "rating": 5, "comment": "Niacinamide brightens skin, reduces oil production, and minimizes pores. Affordable option for oily and acne-prone skin."}
        ],
        "transparency": 5
    },
    {
        "id": 6,
        "brand": "Bioderma",
        "name": "Sensibio H2O Micellar Water",
        "price": 14.99,
        "description": "Gentle cleansing and makeup removing micellar water for sensitive skin",
        "categories": ["cleansing", "sensitive_skin", "trending"],
        "image": "/static/images/5.jpg",
        "benefits": [
            "Removes makeup and impurities",
            "Soothes sensitive skin",
            "No-rinse formula",
            "Maintains skin's natural balance"
        ],
        "ingredients": [
            "Water",
            "PEG-6 Caprylic/Capric Glycerides",
            "Cucumber Fruit Extract",
            "Mannitol"
        ],
        "reviews": [
            {"name": "Dr. Shereene Idriss ✅", "rating": 5, "comment": "Gentle yet effective for removing makeup and cleansing sensitive skin. Fragrance-free formula is dermatologist recommended."}
        ],
        "transparency": 4
    },
    {
        "id": 7,
        "brand": "Beauty of Joseon",
        "name": "Glow Serum: Propolis + Niacinamide",
        "price": 17.99,
        "description": "Brightening and soothing serum enriched with propolis and niacinamide for radiant skin",
        "categories": ["brightening", "hydration", "trending"],
        "image": "/static/images/9.jpg",
        "benefits": [
            "Brightens dull skin",
            "Soothes irritation",
            "Hydrates and nourishes",
            "Improves skin texture"
        ],
        "ingredients": [
            "Propolis Extract",
            "Niacinamide",
            "Panthenol",
            "Sodium Hyaluronate"
        ],
        "reviews": [
            {"name": "Dr. Dray ✅", "rating": 5, "comment": "Combines niacinamide and propolis for hydration and skin brightening. Great for dull, uneven skin tone."}
        ],
        "transparency": 3
    },
    {
        "id": 8,
        "brand": "I'm From",
        "name": "Mugwort Essence",
        "price": 38.00,
        "description": "A soothing and hydrating essence made with 100% mugwort extract to calm and nourish sensitive skin",
        "categories": ["soothing", "hydration", "sensitive_skin"],
        "image": "/static/images/6.jpg",
        "benefits": [
            "Calms redness and irritation",
            "Deeply hydrates the skin",
            "Improves skin texture",
            "Rich in antioxidants"
        ],
        "ingredients": [
            "Mugwort Extract",
            "Glycerin",
            "Butylene Glycol",
            "Betaine"
        ],
        "reviews": [
            {"name": "Dr. Shereene Idriss ✅", "rating": 5, "comment": "100% mugwort extract calms redness and hydrates sensitive, inflamed skin. Perfect for skin in need of soothing."}
        ],
        "transparency": 2
    },
    {
        "id": 9,
        "brand": "La Roche-Posay",
        "name": "Cicaplast Baume B5",
        "price": 14.99,
        "description": "A multi-purpose soothing balm that calms, protects, and repairs dry, irritated, and sensitive skin",
        "categories": ["soothing", "repairing", "sensitive_skin"],
        "image": "/static/images/7.jpg",
        "benefits": [
            "Repairs and protects the skin barrier",
            "Soothes irritation and redness",
            "Non-greasy and fast-absorbing",
            "Suitable for the whole family, including babies"
        ],
        "ingredients": [
            "Panthenol",
            "Shea Butter",
            "Madecassoside",
            "Zinc Gluconate"
        ],
        "reviews": [
            {"name": "Dr. Dray ✅", "rating": 5, "comment": "Highly effective for soothing redness, repairing skin barrier, and reducing irritation. Great multi-purpose balm."}
        ],
        "transparency": 3
    },
    {
        "id": 10,
        "brand": "Glow Recipe",
        "name": "Watermelon Glow PHA + BHA Toner",
        "price": 44.50,
        "description": "A gentle, hydrating toner with PHA and BHA to refine pores and smooth skin texture",
        "categories": ["hydration", "exfoliation", "trending"],
        "image": "/static/images/10.jpg",
        "benefits": [
            "Refines pores",
            "Gently exfoliates dead skin cells",
            "Hydrates and plumps the skin",
            "Improves skin texture"
        ],
        "ingredients": [
            "Watermelon Extract",
            "Polyhydroxy Acid (PHA)",
            "Beta Hydroxy Acid (BHA)",
            "Hyaluronic Acid"
        ],
        "reviews": [
            {"name": "Dr. Shereene Idriss ✅", "rating": 5, "comment": "PHA and BHA gently exfoliate, refine pores, and hydrate skin. Perfect for combination and oily skin."}
        ],
        "transparency": 4
    },
    {
        "id": 11,
        "brand": "Tatcha",
        "name": "The Water Cream",
        "price": 31.00,
        "description": "A refreshing, oil-free moisturizer that provides lightweight hydration while improving skin's texture and clarity",
        "categories": ["hydration", "luxury", "oil_control"],
        "image": "/static/images/11.jpg",
        "benefits": [
            "Provides lightweight hydration",
            "Refines and smooths skin texture",
            "Non-greasy, oil-free formula",
            "Leaves skin radiant and balanced"
        ],
        "ingredients": [
            "Japanese Purple Rice",
            "Hyaluronic Acid",
            "Okinawa Algae Blend",
            "Panax Ginseng Root Extract"
        ],
        "reviews": [
            {"name": "Dr. Shereene Idriss ✅", "rating": 5, "comment": "Lightweight, oil-free formula hydrates effectively. A luxury option ideal for oily and combination skin types."}
        ],
        "transparency": 3
    },
    {
        "id": 12,
        "brand": "Paula's Choice",
        "name": "Skin Perfecting 2% BHA Liquid Exfoliant",
        "price": 32.00,
        "description": "A cult-favorite leave-on exfoliant with salicylic acid to unclog pores, smooth wrinkles, and even skin tone",
        "categories": ["exfoliation", "acne_control", "sensitive_skin"],
        "image": "/static/images/12.jpg",
        "benefits": [
            "Unclogs and minimizes pores",
            "Smooths fine lines and wrinkles",
            "Evens skin tone",
            "Gentle enough for daily use"
        ],
        "ingredients": [
            "Salicylic Acid",
            "Green Tea Extract",
            "Methylpropanediol",
            "Butylene Glycol"
        ],
        "reviews": [
            {"name": "Dr. Rachel Ho ✅", "rating": 5, "comment": "2% BHA unclogs pores and smoothens skin. Perfect for acne-prone or uneven skin tone."}
        ],
        "transparency": 2
    }
]


@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/progressTracking')
def progress_tracking():
    return render_template('progressTracking.html')

@app.route('/compareProducts')
def compare_products():
    return render_template('compare.html')

@app.route('/ingredients')
def learn_ingredients():
    return render_template('ingredient.html')

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