from app.core.email.send_email import send_email

def send_forgot_password_email(to_email: str, otp: str):
    subject = "🔐 MyBlueThink Password Reset OTP"

    body = f"""
    <html>
        <body>
            <h2>Password Reset Request</h2>
            <p>Hello,</p>

            <p>You requested to reset your password.</p>

            <h3 style="color:blue;">OTP: {otp}</h3>

            <p>This OTP is valid for <b>10 minutes</b>.</p>

            <p>If you did not request this, please ignore this email.</p>

            <br>
            <p>Thanks,<br>MyBlueThink Team</p>
        </body>
    </html>
    """

    send_email(to_email, subject, body)