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

    orderId=aiq_1;
    #for i in orderId:
    for message in messages:
        try:
            mail = service.users().messages().get(userId='me', id=message['id'], format="full").execute()
            c = parse_msg(mail)
            #print("value of c",c)

            file = open("emailbody.html", "w", encoding="utf8")
            file.write(c)
            soup = BeautifulSoup(c, 'html.parser')
            final=soup.getText()
            test = ' '.join(final.split())
            #print(test)
            #print(BeautifulSoup(c, 'html.parser'))
            soup = bool(BeautifulSoup(c, 'html.parser').find())

            sub_value = fetch_subject(message, service)
            print(sub_value)

            if (orderId in test and sub_value == True):
                print(test)
        except Exception as error:
            print('An error occurred while sending email: %s'% error)

    ##print(list)

def parse_msg(msg):
    #print(msg.get("payload"))
    #print(msg.get("payload").get("parts")[0].get("body").get("data"))
    if (msg.get("payload").get("parts")[0].get("body").get("data")):
        return base64.urlsafe_b64decode((msg.get("payload").get("parts")[0].get("body").get("data")).encode("ASCII")).decode("utf-8")
    return msg.get("snippet")



def fetch_subject(message,service):

        subject_val=aiq_2;

        messageheader = service.users().messages().get(userId="me", id=message["id"], format="full",
                                                       metadataHeaders=None).execute()
        headers = messageheader["payload"]["headers"]
        #print(headers)
        for i in headers:
            if(i['name'] == 'Subject' and i['value']==subject_val):
                return True


if __name__ == '__main__':
    main()
