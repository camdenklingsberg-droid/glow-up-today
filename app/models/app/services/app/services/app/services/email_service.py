from flask_mail import Mail, Message

mail = Mail()

def send_streak_warning(user):
    msg = Message(
        subject="Your GlowUp streak is at risk 🔥",
        recipients=[user.email],
        body=f"Hey {user.username}, don't break your streak today!"
    )
    mail.send(msg)
