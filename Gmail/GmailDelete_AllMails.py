from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import pickle
import os.path
import traceback
class GMailModifier:
    def __init__(self):
        print('User Created')
        self.scopes = ['https://mail.google.com/']
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        try:
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json', self.scopes)
                    creds = flow.run_local_server(port=0)
                    with open('token.pickle', 'wb') as token:
                        pickle.dump(creds, token)

            service = build('gmail', 'v1', credentials=creds)
            results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
            messages = results.get('messages', [])
            print(messages)
            #meassageId1='17d7b6fa510a83f2'
            for i in messages:
                meassageId=i['id']
                print(meassageId)
                service.users().messages().delete(userId='me', id=meassageId).execute()
        except Exception as error:
            print(traceback.print_exc())
            print("Error occured while authenticating :-")
            print(error)
        print('GMail API auth completed')



if __name__ == '__main__':

    print('Enter message id of the message to be deleted :-')
    user = GMailModifier()
