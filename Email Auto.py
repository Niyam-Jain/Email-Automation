import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from getpass import getpass
import imaplib
import email
from datetime import datetime

def send_email(sender_email, sender_password, receiver_email, subject, message, attachment_path=None):
    
    email = MIMEMultipart()
    email["From"] = sender_email
    email["To"] = receiver_email
    email["Subject"] = subject

    
    email.attach(MIMEText(message, "plain"))

    
    if attachment_path:
        attachment = MIMEBase("application", "octet-stream")
        with open(attachment_path, "rb") as file:
            attachment.set_payload(file.read())
        encoders.encode_base64(attachment)
        attachment.add_header(
            "Content-Disposition",
            f"attachment; filename= {attachment_path.split('/')[-1]}",
        )
        email.attach(attachment)

    
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.starttls()

    
    smtp_connection.login(sender_email, sender_password)

    
    smtp_connection.send_message(email)

    
    smtp_connection.quit()





def check_emails(email_address, email_password, date):
    

    imap_server = "imap.gmail.com"
    imap_port = 993


    imap_connection = imaplib.IMAP4_SSL(imap_server, imap_port)


    imap_connection.login(email_address, email_password)


    mailbox = "INBOX"
    imap_connection.select(mailbox)


    formatted_date = date.strftime("%d-%b-%Y")


    _, message_numbers = imap_connection.search(None, f'(SINCE "{formatted_date}")')
    message_numbers = message_numbers[0].split()


    for num in message_numbers:
        _, data = imap_connection.fetch(num, "(RFC822)")
        raw_message = data[0][1]
        message = email.message_from_bytes(raw_message)


        subject = message["Subject"]
        sender = message["From"]
        date_received = message["Date"]


        print("Subject:", subject)
        print("Sender:", sender)
        print("Date:", date_received)


        if message.is_multipart():
            for part in message.walk():
                content_type = part.get_content_type()

                if content_type.startswith("application"):
                    attachment_name = part.get_filename()
                    print("Attachment:", attachment_name)

                    # Save the attachment if needed
                    # attachment_data = part.get_payload(decode=True)
                    # with open(attachment_name, "wb") as file:
                    #     file.write(attachment_data)

                elif content_type == "text/plain":
                    message_text = part.get_payload()
                    print("Message:", message_text)

        print("--------------------")

    imap_connection.logout()





user_choise = int(input("DO  you want to :-\n1. SEND E-mails\n2. CHECK E-mails\n"))


if (user_choise == 1):

    sender_email = input("Enter your email: ")
    sender_password = getpass("Enter your password: ")
    
    receiver_email = input("Enter the recipient's email: ")
    
    subject = input("Enter the email subject: ")
    message = input("Enter the email message: ")    
    attachment_path = input("Enter the file path (optional): ")



    send_email(sender_email, sender_password, receiver_email, subject, message, attachment_path)



elif (user_choise == 2):
    
    
    email_address = input("Enter your email address: ")
    email_password = getpass("Enter your email password: ")

    
    date_str = input("Enter the date (YYYY-MM-DD): ")
    date = datetime.strptime(date_str, "%Y-%m-%d")

    
    check_emails(email_address, email_password, date)



else:
    print("Invail input !!")


