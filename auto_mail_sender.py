import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender email information
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email_file = 'sender.key'
recipients_file = 'recipients.txt'

# Email subject and content
subject = 'AUTO MAIL SENDER TEST'

def main():

    #NOTE: IF YOU USE THIS CODE WITH VCODE, OPEN COMMENTS BOTTOM LINES.
    """
    file_location = get_current_directory()
    sender_email_file = file_location + '/auto_mail_sender/sender.key'
    recipients_file = file_location + '/auto_mail_sender/recipients.txt'
    """

    # Read sender information from the file
    with open(sender_email_file, 'r') as f:
        sender_email = f.readline().strip()
        sender_password = f.readline().strip()
        print("User info read")

    # Read the recipient list from the file and send separate emails to each user
    with open(recipients_file, 'r') as f:
        recipients = [line.strip() for line in f.readlines()]
        print("Recipients read")

        for recipient in recipients:
            # Create email content
            message = f"Hello {recipient},\n\nThis is a test email sent automatically."

            # Create the email
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
                print(f"An error occurred while sending the email ({recipient}):", str(e))

            finally:
                # Close the connection to the SMTP server
                server.quit()

def get_current_directory():
    return os.getcwd()

if __name__ == '__main__':
    main()
