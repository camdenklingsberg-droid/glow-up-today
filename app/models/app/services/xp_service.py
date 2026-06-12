def add_xp(user, amount):
    multiplier = 2 if user.plan_type == "pro" else 1
    user.xp += amount * multiplier


def get_level(xp):
    levels = ["Beginner", "Improver", "Advanced", "Elite", "Glow Master"]
    return levels[min(xp // 50, len(levels) - 1)]
