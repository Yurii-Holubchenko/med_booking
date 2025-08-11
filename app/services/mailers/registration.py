import emails, os
from app.core.config import smtp_config
from app.utils.render_template import email_template

def send_confirmation_email(email: str, confirmation_token: str) -> None:
    confirmation_link = f"{os.getenv("APP_URL")}/confirmation?token={confirmation_token}"
    subject = "Confirm your registration on MedBooking"

    html_content = email_template("confirmation.html", {
        "confirmation_link": confirmation_link
    })

    send_email(email, subject, html_content)

def send_email(email: str, subject: str, html_content: str) -> None:
    message = emails.Message(
        subject=subject,
        html=html_content,
        mail_from=(smtp_config.SMTP_FROM_NAME, smtp_config.SMTP_FROM)
    )

    response = message.send(
        to=email,
        smtp={
            "host": smtp_config.SMTP_HOST,
            "port": smtp_config.SMTP_PORT,
            "user": smtp_config.SMTP_USERNAME,
            "password": smtp_config.SMTP_PASSWORD,
            "tls": True
        }
    )

    if response.status_code not in [250, 251]:
        print(f"Error while sending an email {response}")
    else:
        print(f"Email to {email} was sent successfully")
