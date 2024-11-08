import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.logger import log

def send_email(subject, body, to_email="admin@example.com"):
    """Send an email notification to the admin."""
    from_email = "youremail@example.com"
    from_password = "yourpassword"

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.example.com", 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        log(f"Email sent to {to_email} with subject: {subject}", "warning")
        print(f"Email sent to {to_email}")
    except Exception as e:
        log(f"Failed to send email: {e}", "error")
