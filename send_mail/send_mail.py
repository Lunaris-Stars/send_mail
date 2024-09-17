import ssl
import smtplib
from email.message import EmailMessage
import os

class EmailConfig:
    """Email configuration class"""
    SENDER_EMAIL = "lunaris4452@gmail.com"
    SENDER_PASSWORD = "jvyweyxvoznpmndt"  # Consider using environment variables for sensitive data
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 465

class EmailContent:
    """Email content class"""
    TEMPLATES_DIR = "templates"

def create_email(sender_email, receiver_email, subject, body):
    """Create an email message"""
    email = EmailMessage()
    email['From'] = sender_email
    email['To'] = receiver_email
    email['Subject'] = subject
    email.set_content(body)
    return email

def send_email(email):
    """Send an email using SMTP"""
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(EmailConfig.SMTP_SERVER, EmailConfig.SMTP_PORT, context=context) as smtp:
            smtp.login(EmailConfig.SENDER_EMAIL, EmailConfig.SENDER_PASSWORD)
            smtp.sendmail(EmailConfig.SENDER_EMAIL, email['To'], email.as_string())
    except smtplib.SMTPAuthenticationError as e:
        print("Authentication error:", e)
    except smtplib.SMTPException as e:
        print("SMTP error:", e)
    except Exception as e:
        print("An error occurred:", e)

def load_template(template_name):
    """Load an email template from file"""
    template_path = os.path.join(EmailContent.TEMPLATES_DIR, template_name + ".txt")
    try:
        with open(template_path, "r") as f:
            template_content = f.read()
        return template_content
    except FileNotFoundError:
        print(f"Template '{template_name}' not found.")
        return None

def render_template(template_content, **kwargs):
    """Render an email template with placeholders"""
    if template_content is None:
        return None
    for key, value in kwargs.items():
        template_content = template_content.replace("{{" + key + "}}", value)
    return template_content

def main():
    receiver_email = input("Enter the receiver's email: ")
    subject = input("Enter the subject: ")
    template_name = input("Enter the template name (hello or follow_up): ")
    name = input("Enter the name: ")
    sender_name = input("Enter the sender name: ")

    template_content = load_template(template_name)
    if template_content is None:
        print("Cannot send email. Template not found.")
        return

    body = render_template(template_content, name=name, sender=sender_name)
    if body is None:
        print("Cannot send email. Template rendering failed.")
        return

    email = create_email(EmailConfig.SENDER_EMAIL, receiver_email, subject, body)
    send_email(email)
    print("Email sent successfully!")

if __name__ == "__main__":
    main()