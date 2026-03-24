from flask import Flask, render_template, request, redirect, url_for

def create_app():
    app = Flask(__name__, template_folder="../")

    sample_listings = [
        {"id": 1, "title": "Modern Miami Waterfront Condo", "city": "Miami, FL", "price": "$689,000", "beds": 3, "baths": 2, "sqft": 1940, "type": "Condo", "tag": "Featured", "desc": "Luxury waterfront condo with skyline views, strong walkability, and premium finishes."},
        {"id": 2, "title": "Atlanta Multifamily Investment", "city": "Atlanta, GA", "price": "$1,180,000", "beds": 6, "baths": 4, "sqft": 6200, "type": "Multifamily", "tag": "Investor Deal", "desc": "Value-add multifamily opportunity in a growing neighborhood with strong rental demand."},
        {"id": 3, "title": "Toronto Furnished Rental", "city": "Toronto, ON", "price": "$3,250/mo", "beds": 2, "baths": 2, "sqft": 980, "type": "Rental", "tag": "Rental", "desc": "Transit-friendly furnished rental with flexible lease options in a high-demand area."},
        {"id": 4, "title": "London Family Townhome", "city": "London, UK", "price": "$845,000", "beds": 4, "baths": 3, "sqft": 2420, "type": "Townhome", "tag": "Family Pick", "desc": "Spacious townhome with strong schools, private garden, and family-friendly layout."},
    ]

    sample_agents = [
        {"name": "Sofia Bennett", "market": "Miami, FL", "specialty": "Luxury + relocation", "plan": "Agent Pro"},
        {"name": "Daniel Reed", "market": "Atlanta, GA", "specialty": "Investment properties", "plan": "Investor Network"},
        {"name": "Nina Patel", "market": "Toronto, ON", "specialty": "Rentals + furnished housing", "plan": "Agent Pro"},
    ]

    @app.route("/")
    def home():
        return render_template("home.html", listings=sample_listings, agents=sample_agents)

    @app.route("/listings")
    def listings():
        q = request.args.get("q", "").lower().strip()
        filtered = sample_listings
        if q:
            filtered = [
                x for x in sample_listings
                if q in x["title"].lower() or q in x["city"].lower() or q in x["type"].lower()
            ]
        return render_template("listings.html", listings=filtered, q=q)

    @app.route("/listing/<int:listing_id>")
    def listing_detail(listing_id):
        listing = next((x for x in sample_listings if x["id"] == listing_id), None)
        if not listing:
            return redirect(url_for("listings"))
        return render_template("listing_detail.html", listing=listing)

    @app.route("/agents")
    def agents():
        return render_template("agents.html", agents=sample_agents)

    @app.route("/pricing")
    def pricing():
        return render_template("pricing.html")

    @app.route("/buyers", methods=["GET", "POST"])
    def buyers():
        success = request.method == "POST"
        return render_template("buyers.html", success=success)

    @app.route("/dashboard")
    def dashboard():
        stats = {
            "active_listings": len(sample_listings),
            "featured_agents": len(sample_agents),
            "buyer_signups": 84,
            "seller_submissions": 39,
            "monthly_leads": 217,
        }
        return render_template("dashboard.html", stats=stats, listings=sample_listings)

    return app
