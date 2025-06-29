
import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from listen_new_message import start_pubsub_listener

from dotenv import load_dotenv

load_dotenv()

topic_name=os.getenv("topic_name")
SCOPES =os.getenv("SCOPES")


def get_service():
  try:
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    return build("gmail", "v1", credentials=creds)
  except:
    print("unable to get service")





def watch_gmail(service):

    body = {
        "labelIds": ["INBOX"],  # Watch for changes in the INBOX
        "topicName": topic_name
    }
    try:
        resp = service.users().watch(userId="me", body=body).execute()
        print(f"Watch registered. Expires: {resp['expiration']}")
        print(f"Start historyId : {resp['historyId']}")
        return resp["historyId"]
    except HttpError as error:
        print(f"An error occurred while setting up Gmail watch: {error}")
        return None





if __name__ == "__main__":

    service = get_service()

    print("\nSetting up Gmail Watch and Pub/Sub Listener...")
    history_id = watch_gmail(service)
    if history_id:
        start_pubsub_listener(history_id)
    else:
        print("Failed to set up Gmail watch. Cannot listen for new messages.")