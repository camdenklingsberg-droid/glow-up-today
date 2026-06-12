import stripe
from flask import Blueprint, redirect

billing_bp = Blueprint("billing", __name__)

stripe.api_key = "YOUR_STRIPE_SECRET_KEY"

@billing_bp.route("/upgrade")
def upgrade():
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {"name": "GlowUp PRO"},
                "unit_amount": 999,
            },
            "quantity": 1,
        }],
        mode="subscription",
        success_url="http://localhost:5000/",
        cancel_url="http://localhost:5000/",
    )

    return redirect(session.url)
