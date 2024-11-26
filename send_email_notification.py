import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import argparse
import logging

# Set up logging
logging.basicConfig(
    filename='email_notification.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def send_email(status):
    """
    Sends an email based on the test status (success or failure).

    Args:
        status (str): Test status, either 'success' or 'failure'.
    """
    sender_email = os.environ.get("SENDER_EMAIL")
    sender_password = os.environ.get("SENDER_PASSWORD")
    recipient_email = os.environ.get("RECIPIENT_EMAIL")

    if not sender_email or not sender_password or not recipient_email:
        logging.error("Email credentials or recipient email are missing.")
        print("Error: Email credentials or recipient email are missing. Check environment variables.")
        return

    # Set email subject and body based on test status
    if status == "success":
        subject = "Selenium Tests Passed ✅"
        body = """
        Dear Team,

        All Selenium tests have passed successfully. 

        You can review the detailed test reports in the attached artifacts or CI/CD logs.

        Best regards,
        Automation Team
        """
    elif status == "failure":
        subject = "Selenium Tests Failed ❌"
        body = """
        Dear Team,

        One or more Selenium tests have failed. 

        Please review the detailed logs and test reports attached in the artifacts to investigate the issues.

        Best regards,
        Automation Team
        """
    else:
        logging.error(f"Invalid test status: {status}")
        print(f"Error: Invalid test status '{status}'.")
        return

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish a connection with the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Log in using app password
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Send the email

        logging.info(f"Email sent successfully to {recipient_email} with status: {status}.")
        print(f"Email sent successfully to {recipient_email} with status: {status}.")

    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
        print(f"Failed to send email: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send email notification for Selenium tests.")
    parser.add_argument('--status', required=True, help="Test status: 'success' or 'failure'")
    args = parser.parse_args()

    send_email(args.status)
