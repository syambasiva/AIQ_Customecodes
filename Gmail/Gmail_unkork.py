import requests
import base64
import pickle
import os.path
from bs4 import BeautifulSoup




from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    ##print(results)
    messages = results.get('messages', [])
    messages1 = results.get('resultSizeEstimate', [])
    #print(messages1)
    #print(messages)
    list = []
    for message in messages:
        list.append(message['id'])
        mail = service.users().messages().get(userId='me', id=message['id'], format="full").execute()
        c = parse_msg(mail)
        test = ' '.join(c.split())
        print(test,"\n",end='')
    print(list)

def parse_msg(msg):
    if msg.get("payload").get("body").get("data"):
        return base64.urlsafe_b64decode(msg.get("payload").get("body").get("data").encode("ASCII")).decode("utf-8")
    return msg.get("snippet")



if __name__ == '__main__':
    main()