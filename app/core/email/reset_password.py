from app.core.email.send_email import send_email

def send_reset_success_email(to_email: str, name: str):
    subject = "✅ Password Reset Successful"

    body = f"""
    <html>
        <body>
            <h2>Password Changed Successfully</h2>

            <p>Hello {name},</p>

            <p>Your password has been successfully updated.</p>

            <p>If you did NOT perform this action, please contact support immediately.</p>

            <br>
            <p>Thanks,<br><b>MyBlueThink Team</b></p>
        </body>
    </html>
    """

    send_email(to_email, subject, body)