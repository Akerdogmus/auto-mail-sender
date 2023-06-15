import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email sender information
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email_file = 'auto_mail_sender/sender.txt'
recipients_file = 'auto_mail_sender/recipients.txt'

# Email subject
subject = 'AUTO MAIL SENDER TEST'

# Read sender information from file
with open(sender_email_file, 'r') as f:
    sender_email = f.readline().strip()
    sender_password = f.readline().strip()
    print("User info read")

# Read recipient list from file and send separate emails to each recipient
with open(recipients_file, 'r') as f:
    recipients = [line.strip() for line in f.readlines()]
    print("Recipients read")

    for recipient in recipients:
        # Create email content
        message = f"Hello {recipient},\n\nThis is a test email sent automatically."

        # Create email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        print(f"Email created and sending to {recipient}.")

        # Connect to the SMTP server and log in
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)

            # Send the email
            server.sendmail(sender_email, recipient, msg.as_string())
            print(f"Email successfully sent to {recipient}!")

        except smtplib.SMTPException as e:
            print(f"SMTP Error ({recipient}):", str(e))

        except Exception as e:
            print(f"An error occurred while sending email to {recipient}:", str(e))

        finally:
            # Close the connection to the SMTP server
            server.quit()
