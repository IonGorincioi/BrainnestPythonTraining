''' You work at a company that sends daily reports to clients via email.
The goal of this project is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:

   1. Use the smtplib library to connect to the email server and send the emails.

   2. Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.

   3. Use the os library to access the report files that need to be sent.

   4. Use a for loop to iterate through the list of recipients and send the email and attachment.

   5. Use the schedule library to schedule the script to run daily at a specific time.

   7. You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''

import smtplib
import ssl

port = 465
sender = input("Email: ")
password = input('Password:')
receiver = input("Receiver email: ")


content = """\

subject: "This is the subject"

          Here is the content of the email.
          Hi!
          """

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, content)


print("Email sent!")
