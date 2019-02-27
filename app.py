from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from flask import Flask, render_template, request

app = Flask(
    __name__,
    template_folder="build",
    static_folder="build/static",
)

SCOPES = ['https://www.googleapis.com/auth/documents',
          'https://www.googleapis.com/auth/drive.appdata',
          'https://www.googleapis.com/auth/drive']


# The ID of a sample document.
DOCUMENT_ID = '1FOrHyHTlRTC6MWIjdAIGvGGOfUNTJwEgWXbQ_QYT7hM'

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/drive", methods=["POST"])
@app.route("/drive", methods=["POST"])
def upload_to_drive():
    body = request.get_json()
    print(body.get('amount'))

    creds = None
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
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('docs', 'v1', credentials=creds, cache_discovery=False)


    # create doc

    # title = 'My Document'
    # body = {
    #     'title': title
    # }
    # doc = service.documents().create(body=body).execute()
    doc = service.documents().get(documentId=DOCUMENT_ID).execute()
    # add text
    requests = [
         {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': 'Title added from flask app '
            }
        }
    ]

    result = service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()
    print('String appended to {0}'.format(doc.get('title')))
    return "Done"
