from PIL import ImageGrab
import time

import base64
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
import mimetypes
import pickle
import os
from apiclient import errors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://mail.google.com/']


def get_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8001)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    return service

def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id,
                body=message).execute()

        print('Message Id: {}'.format(message['id']))

        return message
    except Exception as e:
        print('An error occurred: {}'.format(e))
        return None


def create_message_with_attachment(
    sender,
    to,
    subject,
    message_text,
    file,
    ):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    msg = MIMEText(message_text)
    message.attach(msg)

    (content_type, encoding) = mimetypes.guess_type(file)

    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'

    (main_type, sub_type) = content_type.split('/', 1)

    if main_type == 'text':
        with open(file, 'rb') as f:
            msg = MIMEText(f.read().decode('utf-8'), _subtype=sub_type)

    elif main_type == 'image':
        with open(file, 'rb') as f:
            msg = MIMEImage(f.read(), _subtype=sub_type)
        
    elif main_type == 'audio':
        with open(file, 'rb') as f:
            msg = MIMEAudio(f.read(), _subtype=sub_type)
        
    else:
        with open(file, 'rb') as f:
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(f.read())

    filename = os.path.basename(file)
    msg.add_header('Content-Disposition', 'attachment',
                   filename=filename)
    message.attach(msg)

    raw_message = \
        base64.urlsafe_b64encode(message.as_string().encode('utf-8'))
    return {'raw': raw_message.decode('utf-8')}



now = time.localtime()
time = "%04d-%02d-%02d-%02dh-%02dm-%02ds" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

img=ImageGrab.grab()
saveas="{}{}".format(time,'.png')
img.save(saveas)




 

if __name__ == "__main__":
    service = get_service()
    user_id = 'me'
    msg = create_message_with_attachment('lucykorea@gmail.com', 'lucykorea@gmail.com', '현장미션 완료!!','This is the message body', saveas)
    send_message(service, user_id, msg)