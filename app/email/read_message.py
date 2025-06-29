import base64
from googleapiclient.errors import HttpError



def read_message_detail(service, message_id):

    try:
        msg = service.users().messages().get(userId='me', id=message_id, format='full').execute()

        # Headers
        headers = msg['payload'].get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), '(No Sender)')

        body = ''
        payload = msg['payload']
        parts = payload.get('parts', [])

        for part in parts:
            if part['mimeType'] == 'text/plain' and 'data' in part['body']:
                body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                break
            elif part['mimeType'] == 'multipart/alternative':
                for sub_part in part.get('parts', []):
                    if sub_part['mimeType'] == 'text/plain' and 'data' in sub_part['body']:
                        body = base64.urlsafe_b64decode(sub_part['body']['data']).decode('utf-8')
                        break
                if body:
                    break
        else: # If no text/plain body found, try to get from data directly if available
            if 'data' in payload['body']:
                body = base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8')


        print(f"✉️ From: {sender}")
        print(f"📌 Subject: {subject}")
        print(f"📄 Body:\n{body}\n{'-'*40}")

    except HttpError as error:
        print(f"An error occurred while reading message detail: {error}")


def get_messages(service, query=""):
 
    try:
        results = service.users().messages().list(userId="me", q=query).execute()
        messages = results.get("messages", [])
        return messages
    except HttpError as error:
        print(f"An error occurred: {error}")
        return []
    
    
def fetch_new_messages(service,start_history_id):
    """
    Fetches and prints details of new messages that arrived since the given historyId.
    """
    try:
        # Fetch history records since the startHistoryId, specifically for messageAdded events
        resp = service.users().history().list(
            userId="me",
            startHistoryId=start_history_id,
            historyTypes=["messageAdded"]
        ).execute()

        history_records = resp.get("history", [])
        if not history_records:
            print("No new messages found since last historyId.")
            return

        print("\n--- New Messages ---")
        for h_record in history_records:
            if "messagesAdded" in h_record:
                for message_added_event in h_record.get("messagesAdded", []):
                    message_id = message_added_event["message"]["id"]
                    # Get full details of the new message
                    read_message_detail(service, message_id)

    except HttpError as e:
        print(f"History fetch error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred in fetch_new_messages: {e}")