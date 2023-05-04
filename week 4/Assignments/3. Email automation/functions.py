import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


def send_email(smtp_server, port, sender, password, receiver, subject, message, file_path):
    # find a file and attach it to the email
    em = MIMEMultipart()
    em['From'] = sender
    em['To'] = receiver
    em['Subject'] = subject
    em.attach(MIMEText(message, "html"))  # attach the message to all the other email's parts

    attachment = open(file_path, "rb")
    attachment_package = MIMEBase('application', 'octet-stream')
    attachment_package.set_payload(attachment.read())
    attachment_package.add_header('Content-Disposition', 'attachment', filename=file_path)
    em.attach(attachment_package)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, em.as_string())
        print("Email sent!")