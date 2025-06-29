
import base64
from email.message import EmailMessage
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

load_dotenv()

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
        print(f"Message sent, ID: {sent_message['id']}")
        return sent_message
    except HttpError as error:
        print(f"An error occurred while sending message: {error}")
        return None
