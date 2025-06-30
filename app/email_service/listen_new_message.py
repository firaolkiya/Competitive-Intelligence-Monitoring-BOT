
import json
from google.cloud import pubsub_v1
import os
from email_service.manage_cursor import save_cursor,load_cursor
from email_service.read_message import fetch_new_messages
from dotenv import load_dotenv

load_dotenv()

topic_name= os.getenv("topic_name")
PROJECT_ID = os.getenv("PROJECT_ID")
SUB_ID  = os.getenv("SUB_ID")

def start_pubsub_listener(service):
    if not PROJECT_ID or not SUB_ID:
        print("setup failed")
        return 
    try:
      subscriber = pubsub_v1.SubscriberClient()
      sub_path = subscriber.subscription_path(PROJECT_ID , SUB_ID)
    except Exception as e:
      print(f"error occerd.. {e}")
      return

    try:
        subscriber.get_subscription(request={"subscription": sub_path})
        print(f"Pub/Sub subscription '{SUB_ID}' already exists.")
    except Exception:
        print(f"Pub/Sub subscription '{SUB_ID}' does not exist, creating...")
        try:
            subscriber.create_subscription(request={"name": sub_path, "topic": topic_name})
            print(f"Pub/Sub subscription '{SUB_ID}' created successfully.")
        except Exception as create_error:
            print(f"Error creating Pub/Sub subscription: {create_error}")
            return

    def callback(msg):
      data = json.loads(msg.data.decode("utf-8"))
      new_history = int(data["historyId"])
      msg.ack()

      last_history = load_cursor()
      if last_history is None:
          save_cursor(new_history)
          print(f"🔔 First push received (historyId={new_history}) – bookmark set.")
          return

      print(f"\n🔔 Gmail pushed, historyId={new_history}  (fetching from {last_history})")
      fetch_new_messages(service,last_history)          # use OLD cursor
      save_cursor(new_history)     

    streaming_pull = subscriber.subscribe(sub_path, callback=callback)
    print(f"\nListening for new-mail notifications on {sub_path} ... (Ctrl-C to stop)")
    try:
        streaming_pull.result() # Blocks until the subscription is cancelled or an error occurs
    except KeyboardInterrupt:
        streaming_pull.cancel()
        print("Listener stopped.")
    except Exception as e:
        print(f"An error occurred in the Pub/Sub listener: {e}")

