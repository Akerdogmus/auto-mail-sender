# Auto Mail Sender Repository

This repository contains a Python script for automatically sending emails using the smtplib library. The script reads the sender's email address and password from a file, and the recipient list from another file. It then sends individual emails to each recipient using the SMTP protocol.

Features:
- Reads sender's email address and password from a file for secure access
- Reads recipient list from a file, allowing customization and flexibility
- Sends personalized emails to each recipient
- Handles SMTP errors and exceptions gracefully

Usage:
1. Set up the sender's email address and password in the 'sender.txt' file.
2. Add the recipient email addresses in the 'recipients.txt' file, with each address on a new line.
3. Run the script to send emails to all recipients.

Note: Make sure to enable less secure apps or generate an app password if using Gmail as the SMTP server.

This script is a useful tool for sending automated emails for various purposes, such as notifications, reminders, newsletters, or any other scenario that requires bulk or automated email communication.

Contributions and improvements are welcome! Feel free to fork the repository and submit pull requests to enhance the functionality or add new features.

NOTE: For using your Gmail services for this, please change your account settings right below:
Login to your email account -> click manage account -> security -> turn on 2 step verification -> go back to security page and click app passwords (https://myaccount.google.com/apppasswords) -> in select app choose "other" -> paste "WP Mail SMTP" and click generate-> copy the password to the code


Let's automate your email communication with the Auto Mail Sender script!

