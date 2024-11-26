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
         "reviews" : [
            {"name" : "Anna", "rating": 5, "comment": "I recently added a centella serum to my skincare routine, and it’s been a game-changer for my sensitive skin. The scent is light and natural, making it pleasant to use without any overpowering fragrance. It’s easy to use and it absorbs quickly." },
            {"name" : "Rebecca", "rating" : 4, "comment":"I can say that this works for sensitive, oily, acne prone skin, and also to other types. Those particularly are my skin type, and this ampoule worked wonders on my face. " },
            {"name" : "Meagan", "rating" : 4, "comment": "Received this product 2 days ago. My makeup that evening was better, my face felt so much better and after that nighttime facial cleanse that same night, I am not gonna lie, my skin looked so clean and shiny & not in an oily way"}
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
        "reviews" : [
            {"name" : "Isabelle", "rating": 5, "comment": "So I have VERY sensative combination skin, and I am VERY fungal acne prone, so naturally finding a good moisturizer has been a struggle. But THIS STUFF IS MY HOLY GRAIL!!" },
            {"name" : "Grace", "rating" : 4, "comment":" Good, but I like the CIca Recovery cream better" },
            {"name" : "Ashley", "rating" : 2, "comment": " Not the best for REALLY dry skin"}
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
        "reviews" : [
            {"name" : "Anna", "rating": 3, "comment": "This stuff is a bit sticky. Overall I do like it." },
            {"name" : "Isabelle", "rating" : 4, "comment":" Really nice product, it leaves my skin glowing for a long period of time" },
            {"name" : "Grace", "rating" : 5, "comment": " I use this every day and it's made a huge difference in my skin! It's hydrating and my sensitive skin doesn't react to it. My skin glows now and my pores seem smaller. A must have!"}
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
    "reviews": [
        {
            "name": "Sarah",
            "rating": 5,
            "comment": "This toner is a game changer for my sensitive skin! It's so calming and refreshing."
        },
        {
            "name": "Jin",
            "rating": 4,
            "comment": "I like the lightweight texture and how quickly it absorbs. Great for layering."
        },
        {
            "name": "Amara",
            "rating": 5,
            "comment": "I use this toner daily, and it has significantly reduced redness on my cheeks. Highly recommend!"
        }
    ],
    "transparency": 4
},
    {
    "id": 5,
    "brand": "The Ordinary",
    "name": "Niacinamide 10% + Zinc 1%",
    "price": 6.50,
    "description": "High-strength vitamin and mineral formula to reduce the appearance of blemishes and congestion",
    "categories": ["oil_control", "brightening", "trending"],
    "image": "/static/images/4.jpg",
    "benefits": [
        "Regulates sebum production",
        "Minimizes appearance of pores",
        "Reduces redness and blemishes",
        "Brightens skin tone"
    ],
    "reviews": [
        {
            "name": "Emma",
            "rating": 5,
            "comment": "I've been using this for months, and it's made a noticeable difference in my skin texture and oil control."
        },
        {
            "name": "Liam",
            "rating": 4,
            "comment": "Great product for the price. It helps with my blemishes, but it can feel a bit sticky."
        },
        {
            "name": "Sophia",
            "rating": 5,
            "comment": "My holy grail! It has helped reduce the redness and keeps my skin smooth."
        }
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
    "reviews": [
        {
            "name": "Alice",
            "rating": 5,
            "comment": "This is my go-to makeup remover! It's gentle and doesn't irritate my skin."
        },
        {
            "name": "Mark",
            "rating": 4,
            "comment": "Cleanses well without any greasy residue. Great for everyday use."
        },
        {
            "name": "Sophie",
            "rating": 5,
            "comment": "Perfect for my sensitive skin. Leaves my face feeling fresh and clean!"
        }
    ],
    "transparency": 4
},   {
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
    "reviews": [
        {
            "name": "Evelyn",
            "rating": 5,
            "comment": "This serum has transformed my skin! It gives me such a healthy glow without feeling heavy."
        },
        {
            "name": "Ryan",
            "rating": 4,
            "comment": "I like how hydrating it is, and it absorbs well. My skin feels smoother after just a few uses."
        },
        {
            "name": "Isabella",
            "rating": 5,
            "comment": "Love this product! The niacinamide has helped even out my skin tone, and the propolis is so soothing."
        }
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
    "reviews": [
        {
            "name": "Olivia",
            "rating": 5,
            "comment": "This essence is a lifesaver for my sensitive skin. It's so calming and absorbs beautifully."
        },
        {
            "name": "Daniel",
            "rating": 4,
            "comment": "I love how natural and gentle this feels. It works great as part of my hydration routine."
        },
        {
            "name": "Emily",
            "rating": 5,
            "comment": "I've noticed such an improvement in my skin texture! Perfect for anyone with redness or irritation."
        }
    ],
    "transparency": 2
},
      {
    "id": 7,
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
    "reviews": [
        {
            "name": "James",
            "rating": 5,
            "comment": "This balm is amazing for dry patches and irritation. It’s a staple in my skincare routine."
        },
        {
            "name": "Hannah",
            "rating": 5,
            "comment": "Super versatile! I use it on my face and hands, especially during winter. Highly recommend."
        },
        {
            "name": "Ethan",
            "rating": 4,
            "comment": "Great for soothing redness, but it takes a bit longer to absorb than I expected."
        }
    ],
    "transparency": 3
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