############################################################################
## Gmail mail sending functions - using python3
## REF: https://developers.google.com/gmail/api/guides/sending
## Valid as of Jun 5, 2019
## Author: Dhruv Joshi
############################################################################
# setup the email infrastructure
from __future__ import print_function
import base64
from email.mime.text import MIMEText
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('/home/dhruv_joshi_1989/usdinr/token.pickle'):
    with open('/home/dhruv_joshi_1989/usdinr/token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            '/home/dhruv_joshi_1989/usdinr/credentials.json', SCOPES)
        creds = flow.run_local_server()
    # Save the credentials for the next run
    with open('/home/dhruv_joshi_1989/usdinr/token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('gmail', 'v1', credentials=creds)

def create_message(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text, 'html')
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def send_message(service, user_id, message):
  """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
  message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
  print('Message Id: %s' % message['id'])
  return message

