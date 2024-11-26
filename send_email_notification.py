import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
import sys

# Set up logging
logging.basicConfig(
    filename='email_notification.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def send_email(subject, body, recipient_emails):
    """
    Sends an email with the specified subject and body to the recipients.

    Args:
        subject (str): Subject of the email.
        body (str): Body of the email.
        recipient_emails (list): List of recipient email addresses.
    """
    # Sender credentials
    sender_email = "antonysilvesta74@gmail.com"
    sender_password = "tyoy vegp ukgm pewe"  # Use the App Password

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipient_emails)  # Join multiple recipients with commas
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish a connection with the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Log in using app password
            server.sendmail(sender_email, recipient_emails, msg.as_string())  # Send the email

        logging.info(f"Email sent successfully to {', '.join(recipient_emails)}!")
        print(f"Email sent successfully to {', '.join(recipient_emails)}!")

    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
        print(f"Failed to send email: {e}")


def get_email_content(test_result):
    """
    Generates email subject and body based on the test result.

    Args:
        test_result (str): Result of the test, either "pass" or "fail".

    Returns:
        tuple: Subject and body for the email.
    """
    if test_result == "pass":
        subject = "Selenium Test Passed ✅"
        body = """
        Dear Team,

        The Selenium scripts have been executed successfully, and all tests passed.

        Best regards,
        Automation Team
        """
    elif test_result == "fail":
        subject = "Selenium Test Failed ❌"
        body = """
        Dear Team,

        The Selenium scripts encountered failures during execution. Please review the logs for more details.

        Best regards,
        Automation Team
        """
    else:
        subject = "Selenium Test Notification"
        body = """
        Dear Team,

        The Selenium test run completed, but the result is unknown. Please check the logs for details.

        Best regards,
        Automation Team
        """
    return subject, body


if __name__ == "__main__":
    # Get the test result from command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python send_email_notification.py <test_result>")
        print("Where <test_result> is either 'pass' or 'fail'")
        sys.exit(1)

    test_result = sys.argv[1].lower()
    if test_result not in ["pass", "fail"]:
        print("Invalid test result. Use 'pass' or 'fail'.")
        sys.exit(1)

    # Generate email content based on the test result
    subject, body = get_email_content(test_result)

    # Define recipients
    recipient_emails = ["antony.silvesta@nidrive.in"]

    # Send the email
    send_email(subject, body, recipient_emails)
