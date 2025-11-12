# main.py
import os
from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_ADDRESS = os.getenv("TO_ADDRESS")

def send_email(subject: str, body: str):
    """Send an email using SMTP credentials from .env"""
    if not all([SMTP_HOST, SMTP_PORT, EMAIL_ADDRESS, EMAIL_PASSWORD, TO_ADDRESS]):
        raise SystemExit("❌ Missing SMTP configuration in .env file")

    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_ADDRESS
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    subject = "Test Email from Auto Emailer"
    body = "Hello! This is a test email sent from my Python auto emailer project."
    send_email(subject, body)
