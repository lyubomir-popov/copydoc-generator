from __future__ import print_function
import pickle
from os import environ, path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import datetime

app = Flask(
    __name__,
    template_folder="build",
    static_folder="build/static",
)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

SCOPES = ['https://www.googleapis.com/auth/documents',
          'https://www.googleapis.com/auth/drive.appdata',
          'https://www.googleapis.com/auth/drive']


# The ID of the document to edit.
DOCUMENT_ID = environ['DOCUMENT_ID']

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/drive", methods=["POST"])
@app.route("/drive", methods=["POST"])
@cross_origin()
def append_text():
    body = request.get_json()

    creds = None
    if path.exists('token.pickle'):
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
    # print(body.get('heading'))
    heading = body.get('heading')
    heading_length = len(heading)
    date = datetime.datetime.now().strftime("%y/%m/%d")
    # add text
    requests = [
        {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': heading
            }
        },
        {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': 1,
                    'endIndex': heading_length
                },
                'paragraphStyle': {
                    'namedStyleType': 'TITLE'
                },
                'fields': 'namedStyleType'
            }
        }, {
            'updateTextStyle': {
                'range': {
                    'startIndex': 1,
                    'endIndex': heading_length
                },
                'textStyle': {
                    'weightedFontFamily': {
                        'fontFamily': 'Ubuntu'
                    }
                },
                'fields': 'weightedFontFamily'
            }
        }
    ]

    result = service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()
    print('String appended to {0}'.format(doc.get('title')))
    return "Done"
