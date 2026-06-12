from flask import Blueprint, request, render_template
from flask_login import login_required, current_user
from ..services.task_service import get_tasks
from ..services.xp_service import add_xp, get_level

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET", "POST"])
@login_required
def dashboard():
    plan = None

    if request.method == "POST":
        goal = request.form.get("goal")
        plan = get_tasks(goal, current_user)

        add_xp(current_user, len(plan) * 10)

    return render_template(
        "dashboard.html",
        user=current_user,
        plan=plan,
        level=get_level(current_user.xp)
    )
