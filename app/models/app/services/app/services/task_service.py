TASKS = {
    "skin": ["Wash face", "Drink water", "Use sunscreen"],
    "style": ["Clean outfit", "Fix hairstyle"],
    "fitness": ["Walk 20 min", "Pushups"],
    "confidence": ["Eye contact", "Talk to someone"]
}

PRO_TASKS = ["AI Glow Plan (beta)", "Advanced Analytics"]

def get_tasks(goal, user):
    tasks = TASKS.get(goal, [])

    if user.plan_type == "pro":
        tasks += PRO_TASKS

    return tasks
