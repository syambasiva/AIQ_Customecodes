import requests
import base64
import pickle
import os.path
from bs4 import BeautifulSoup

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])
    messages1 = results.get('resultSizeEstimate', [])
    list = []
    for message in messages:
        list.append(message['id'])
    print(list)
    msg_id=list[0]
    print(msg_id)
    mail = service.users().messages().get(userId='me', id=msg_id, format="full").execute()
    c = parse_msg(mail)
    print(type(c))
def parse_msg(msg):
    if(msg.get("payload").get("body").get("data")):
        return base64.urlsafe_b64decode((msg.get("payload").get("body").get("data")).encode("ASCII")).decode("utf-8")
    # return msg.get("snippet")

# 182f8f493ae35d24

if __name__ == '__main__':
    main()