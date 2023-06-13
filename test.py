from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

creds = Credentials.from_authorized_user_info(info=info)

# Create an instance of the Gmail API service
service = build('gmail', 'v1', credentials=creds)

# Create a message
message = MIMEMultipart()
message['to'] = 'recipient@example.com'
message['subject'] = 'Fatura vencida'
body = 'A fatura está vencendo, por favor efetue o pagamento.'
message.attach(MIMEText(body,'plain'))

# Send the message
create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
send_message = (service.users().messages().send(userId="me", body=create_message).execute())
