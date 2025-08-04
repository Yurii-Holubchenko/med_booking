def send_confirmation_email(email: str, confirmation_token: str):
    confirmation_link = f"https://app-domain.com/confirm?token={confirmation_token}"
    subject = "Confirm your registration on MedBooking"
    body = f"Click the link to confirm your registration: {confirmation_link}"

    print(f"Email was sent to {email}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
