import json

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
    ##print(messages1)

    list=[]
    for message in messages:
        list.append(message['id'])
    ## aiq_1 format =['2200305188','2200301845','2200303046','2200301848','2200301865'];
    orderId=["2200303549", "2200303100", "2200303100", "2200303549", "2200303549", "2200301852", "2200301852", "2200301852", "2200303549"];
    subject = "An update on your bike order";

    #orderId2 =json.loads(orderId)
    outputbodycontent=[]
    for i in orderId:
        for message in messages:
            try:
                mail = service.users().messages().get(userId='me', id=message['id'], format="full").execute()
                c = parse_msg(mail)
                file = open("emailbody.html", "w", encoding="utf8")
                file.write(c)
                soup = bool(BeautifulSoup(c, 'html.parser').find())
                if soup == True:
                    soup = BeautifulSoup(c, 'html.parser')
                    Final = soup.find_all('table')[0].get_text()
                    test = ' '.join(Final.split())
                    sub_value = fetch_subject(message, service,subject)
                if soup == False:
                    test = ' '.join(c.split())
                    sub_value = fetch_subject(message, service,subject)

                if (i in test and sub_value == True):
                    print(test)
            except Exception as error:
                print('An error occurred while sending email: %s'% error)


def parse_msg(msg):

    if (msg.get("payload").get("parts")[0].get("body").get("data") != None):
        return base64.urlsafe_b64decode(
            (msg.get("payload").get("parts")[0].get("body").get("data")).encode("ASCII")).decode("utf-8")

    if (msg.get("payload").get("parts")[0]['parts'][0]['body'].get("data") != None):
        return base64.urlsafe_b64decode(
            (msg.get("payload").get("parts")[0]['parts'][0]['body'].get("data")).encode("ASCII")).decode("utf-8")

    return msg.get("snippet")

def fetch_subject(message,service,subject):

        messageheader = service.users().messages().get(userId="me", id=message["id"], format="full",
                                                       metadataHeaders=None).execute()
        headers = messageheader["payload"]["headers"]
        for i in headers:
            if (i['name'] == 'Subject' and i['value'] == subject):
                return True



if __name__ == '__main__':
    main()
