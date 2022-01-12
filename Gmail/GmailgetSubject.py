
# connect to gmail api
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():

    # create the credential the first time and save it in token.pickle
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
            creds = flow.run_local_server()
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    #create the service
    service = build('gmail', 'v1', credentials=creds)


    messageheader= service.users().messages().get(userId="me", id=emails["id"], format="full", metadataHeaders=None).execute()
    # print(messageheader)
    headers=messageheader["payload"]["headers"]
    subject= [i['value'] for i in headers if i["name"]=="Subject"]
    print(subject)

if __name__ == '__main__':
    main()