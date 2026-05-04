from email.mime.text import MIMEText
import smtplib
from app.core.config import (
    EMAIL_HOST,
    EMAIL_PORT,
    EMAIL_USE_TLS,
    EMAIL_HOST_USER,
    EMAIL_HOST_PASSWORD
)

def send_email(to_email: str, subject: str, body: str):
    msg = MIMEText(body, "html")   # ✅ HTML enabled
    msg["Subject"] = subject
    msg["From"] = EMAIL_HOST_USER
    msg["To"] = to_email

    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)

    if EMAIL_USE_TLS:
        server.starttls()

    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    server.sendmail(EMAIL_HOST_USER, to_email, msg.as_string())
    server.quit()