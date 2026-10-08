"""
ShelfSense Gemini-Powered Email Dispatcher
Developed by S. M. Mahmud Iqbal
Food Process Engineering & Export Stability Systems

This script uses Google Gemini to personalize and dispatch B2B outreach emails
directly through standard Gmail SMTP.
"""

import os
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_NAME = "S. M. Mahmud Iqbal"

# Fill in your Gmail credentials or set environment variables:
GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS", "your_email@gmail.com")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD", "your_16_char_app_password")

def send_personalized_email(to_email, to_name, subject, body):
    msg = MIMEMultipart()
    msg["From"] = f"{SENDER_NAME} <{GMAIL_ADDRESS}>"
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain", "utf-8"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"✅ Successfully sent to {to_name} ({to_email})")
        return True
    except Exception as e:
        print(f"❌ Failed to send to {to_email}: {e}")
        return False

def run_campaign(csv_path="prospects.csv", dry_run=True):
    print("=" * 60)
    print("ShelfSense Outreach Dispatcher — Developed by S. M. Mahmud Iqbal")
    print(f"Mode: {'DRY RUN (Preview Only)' if dry_run else 'LIVE DISPATCH'}")
    print("=" * 60)

    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            first_name = row.get("first_name", "Director")
            company = row.get("company_name", "your company")
            product = row.get("product_name", "export line")
            target_market = row.get("target_market", "overseas markets")
            email = row.get("email", "")

            subject = f"Export shelf stability review for {company}'s {product}"
            body = f"""Dear {first_name},

I noticed {company} exports {product} into {target_market}.

As a food engineering researcher specializing in preservation kinetics, I developed ShelfSense (https://shelfsense-lemon.vercel.app) — a predictive stability engine that models moisture sorption (Aw), equilibrium pH, and Arrhenius temperature stress during 30-day maritime shipping.

Under equatorial cargo hold transit (32–35°C), moisture vapor transfer often reduces shelf life by 25–40%, risking destination customs rejection.

I would love to run a complimentary, 1-page Shelf Stability Certificate for one of {company}'s export SKUs so your QA team can review the kinetic decay trajectory before your next container ships.

Would you be open to reviewing a sample evaluation?

Best regards,

S. M. Mahmud Iqbal
Food Process & Preservation Engineering
ShelfSense — https://shelfsense-lemon.vercel.app
Developed by S. M. Mahmud Iqbal"""

            print(f"\n[Prospect: {first_name} | {company}]")
            print(f"To: {email}")
            print(f"Subject: {subject}")

            if not dry_run:
                send_personalized_email(email, first_name, subject, body)
            else:
                print("  -> [Dry Run] Email previewed. (Set dry_run=False to dispatch)")

if __name__ == "__main__":
    # Test run in preview mode
    run_campaign(dry_run=True)
