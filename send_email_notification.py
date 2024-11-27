import smtplib
import os
import sys
from email.mime.text import MIMEText

# Get outcome from arguments
if len(sys.argv) < 2:
    print("Error: Outcome argument is required (e.g., success or failure).")
    sys.exit(1)

outcome = sys.argv[1]

# Email configuration from environment variables
sender_email = os.getenv('antonysilvesta74@gmail.com')
sender_password = os.getenv('tyoy vegp ukgm pewe')
recipient_email = os.getenv('antony.silvesta@nidrive.in')

# Validate environment variables
if not sender_email or not sender_password or not recipient_email:
    print("Error: Missing environment variables (SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL).")
    sys.exit(1)

# Email content
subject = f"Test Run {outcome.capitalize()}"
body = f"The test run has {outcome}."
message = MIMEText(body)
message["Subject"] = subject
message["From"] = sender_email
message["To"] = recipient_email

# Send email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
    print(f"Email sent successfully for {outcome} outcome.")
except Exception as e:
    print(f"Failed to send email: {e}")
