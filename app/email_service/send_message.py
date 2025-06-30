
import base64
from email.message import EmailMessage
from googleapiclient.errors import HttpError
from manage_sheet.read_worksheet import read_rows
from dotenv import load_dotenv
import os
load_dotenv()

EMAIL_SHEET_ID =os.getenv("EMAIL_SHEET_ID")
PRODUCT_SHEET_ID =os.getenv("PRODUCT_SHEET_ID")


def send_message(service, sender, to, subject, body):

    message = EmailMessage()
    message.set_content(body)
    message["To"] = to
    message["From"] = sender
    message["Subject"] = subject

    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {"raw": encoded_message}

    try:
        sent_message = service.users().messages().send(userId="me", body=create_message).execute()
        print(f"Message sent, to {to}")
        return sent_message
    except HttpError as error:
        print(f"An error occurred while sending message: {error}")
        return None
    
def send_mult_emails(service,sender,subject,message):
    rows = read_rows(EMAIL_SHEET_ID)
    for row in rows:
        if row['status']=='active':
            try:
                send_message(service=service,sender=sender,to=row["email"],subject=subject,body=message)
            except Exception as e:
                print(f"unable to send email to {row['email']} {e}")
# send_mult_emails()  

        
