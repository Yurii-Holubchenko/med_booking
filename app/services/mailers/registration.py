import emails
from app.core.config import smtp_config

def send_confirmation_email(email: str, confirmation_token: str):
    confirmation_link = f"https://app-domain.com/confirm?token={confirmation_token}"
    subject = "Confirm your registration on MedBooking"
    body = f"Click the <a href='{confirmation_link}'>link</a> to confirm your registration."

    message = emails.Message(
        subject=subject,
        html=body,
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
