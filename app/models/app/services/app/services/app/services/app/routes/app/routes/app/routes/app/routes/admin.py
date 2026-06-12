from flask import Blueprint
from ..models.user import User

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin")
def admin_dashboard():
    users = User.query.all()

    return {
        "total_users": len(users),
        "pro_users": len([u for u in users if u.plan_type == "pro"])
    }
