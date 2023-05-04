''' You work at a company that sends daily reports to clients via email.
The goal of this project is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:

   1. Use the smtplib library to connect to the email server and send the emails.

   2. Use the email library to compose the email, including the recipient's email address,
      the subject, and the body of the email.

   3. Use the os library to access the report files that need to be sent.

   4. Use a for loop to iterate through the list of recipients and send the email and attachment.

   5. Use the schedule library to schedule the script to run daily at a specific time.

   7. You can also set up a log file to keep track of the emails that have been sent and any errors that may have
      occurred during the email sending process. '''

import os
import schedule
from functions import send_email


# def send_email(smtp_server, port, sender, password, receiver, file_path):
#     # find a file and attach it to the email
#     em = MIMEMultipart()
#     em['From'] = sender
#     em['To'] = receiver
#     em['Subject'] = subject
#     em.attach(MIMEText(message, "html"))  # attach the message to all the other email's parts
#
#     attachment = open(file_path, "rb")
#     attachment_package = MIMEBase('application', 'octet-stream')
#     attachment_package.set_payload(attachment.read())
#     attachment_package.add_header('Content-Disposition', 'attachment', filename=file_path)
#     em.attach(attachment_package)
#
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#         server.login(sender, password)
#         server.sendmail(sender, receiver, em.as_string())
#         print("Email sent!")

    # send_email(smtp_server, port, sender, password, receiver, file_path)


# These are fake email addresses.
# real ones are to be added
# recipients = ['someone@gmail.com', 'anyone@gmil.com', 'everyone@gmail.com']
receivers = ['iongorincioi4@gmail.com', 'gorincioidaniel9@gmail.com', 'natiluk82@gmail.com']

# EMAIL_PASSWORD is an environment variable created
# on the system which contains the email password
password = os.environ.get("EMAIL_PASSWORD")
smtp_server = "smtp.gmail.com"
port = 465
sender = "iongorincioi@gmail.com"

subject = "Testing"

message = """
    <h3>Hello there!</h3>
    This is an automated email,
    which is sent only for testing purposes.
    <p>Please, <strong><em>do not reply!!!</em></strong></p>
    """
file_path = r"files/report.txt"

for receiver in receivers:
    receiver = receiver
    print(f"To: {receiver}")
    sending = send_email(smtp_server, port, sender, password, receiver, subject, message, file_path)

