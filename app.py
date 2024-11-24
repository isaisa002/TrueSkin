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
        ],
        "reviews" : [
            {"name" : "Anna", "rating": 5, "comment": "I recently added a centella serum to my skincare routine, and it’s been a game-changer for my sensitive skin. The scent is light and natural, making it pleasant to use without any overpowering fragrance. It’s easy to use and it absorbs quickly." },
            {"name" : "Rebecca", "rating" : 4, "comment":"I can say that this works for sensitive, oily, acne prone skin, and also to other types. Those particularly are my skin type, and this ampoule worked wonders on my face. " },
            {"name" : "Meagan", "rating" : 4, "comment": "Received this product 2 days ago. My makeup that evening was better, my face felt so much better and after that nighttime facial cleanse that same night, I am not gonna lie, my skin looked so clean and shiny & not in an oily way"}
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
        ],
        "reviews" : [
            {"name" : "Isabelle", "rating": 5, "comment": "So I have VERY sensative combination skin, and I am VERY fungal acne prone, so naturally finding a good moisturizer has been a struggle. But THIS STUFF IS MY HOLY GRAIL!!" },
            {"name" : "Grace", "rating" : 4, "comment":" Good, but I like the CIca Recovery cream better" },
            {"name" : "Ashley", "rating" : 2, "comment": " Not the best for REALLY dry skin"}
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
        ],
        "reviews" : [
            {"name" : "Janet", "rating": 1, "comment": "If you have fungal acne please avoid this use tea tree instead" },
            {"name" : "Thao", "rating" : 4, "comment":" Super glow love it. My all time favourite" },
            {"name" : "Sandra", "rating" : 5, "comment": " I love this and I love how it made my skin feel"}
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
        ],
        "reviews" : [
            {"name" : "Janet", "rating": 1, "comment": "If you have fungal acne please avoid this use tea tree instead" },
            {"name" : "Thao", "rating" : 4, "comment":" Super glow love it. My all time favourite" },
            {"name" : "Sandra", "rating" : 5, "comment": " I love this and I love how it made my skin feel"}
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
        ],
        "reviews" : [
            {"name" : "Janet", "rating": 1, "comment": "If you have fungal acne please avoid this use tea tree instead" },
            {"name" : "Thao", "rating" : 4, "comment":" Super glow love it. My all time favourite" },
            {"name" : "Sandra", "rating" : 5, "comment": " I love this and I love how it made my skin feel"}
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
        ],
        "reviews" : [
            {"name" : "Anna", "rating": 3, "comment": "This stuff is a bit sticky. Overall I do like it." },
            {"name" : "Isabelle", "rating" : 4, "comment":" Really nice product, it leaves my skin glowing for a long period of time" },
            {"name" : "Grace", "rating" : 5, "comment": " I use this every day and it's made a huge difference in my skin! It's hydrating and my sensitive skin doesn't react to it. My skin glows now and my pores seem smaller. A must have!"}
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
        ],
        "reviews" : [
            {"name" : "Liliane", "rating": 4, "comment": "I love that it comes with a pump! 1 or 2  pumps and you're good to go. It's super fresh,ligh and lotion-like emulsion." },
            {"name" : "Irwin", "rating" : 4, "comment":" Really nice product, it's my go to cream as i don't like scents" },
            {"name" : "Taylor", "rating" : 5, "comment": " I've been using this face cream for a few weeks now and I'm truly Impressed! The texture is light and aborbs quicly, leaving no greasy residue. It's perfect for both morning and night time use"}
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
        ],
        "reviews" : [
            {"name" : "Janet", "rating": 1, "comment": "If you have fungal acne please avoid this use tea tree instead" },
            {"name" : "Thao", "rating" : 4, "comment":" Super glow love it. My all time favourite" },
            {"name" : "Sandra", "rating" : 5, "comment": " I love this and I love how it made my skin feel"}
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
        ],
        "reviews" : [
            {"name" : "Fatoumata", "rating": 2, "comment": "It didn't work on my rosacea sensitive skin. " },
            {"name" : "Rebecca", "rating" : 5, "comment":" Great for first time users of salicylic acid! Extremely gentle on the skin and does not irritate" },
            {"name" : "Alice", "rating" : 5, "comment": " My all time faveorite. I have been using it since 2020 and always worked very well with my oily and sensitive skin"}
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