from __future__ import print_function
import pickle
from os import environ, path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

import json

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

@app.route("/dump", methods=["POST"])
@cross_origin()
def dump():
    service = get_service()
    result = service.documents().get(documentId=DOCUMENT_ID).execute()
    print(json.dumps(result, indent=4, sort_keys=True), file=open("dump.json", "w"))
    return result

# @app.route("/drive", methods=["POST"])
@app.route("/drive", methods=["POST"])
@cross_origin()
def append_text():
    patterns = request.get_json()

    all_doc_requests = get_doc_requests(patterns)
    service = get_service()
    doc = service.documents().get(documentId=DOCUMENT_ID).execute()

    result = service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': all_doc_requests}).execute()
    print('String appended to {0}'.format(doc.get('title')))
    return "Done"

def get_service():
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

    return service

index = 1

def get_doc_requests(patterns):
    all_doc_requests = []

    for pattern in patterns:
        pattern_type = pattern['type']
        doc_requests = None

        if pattern_type == 'hero':
            doc_requests = handle_hero(pattern)
        # elif pattern_type == 'matrix':

        if not doc_requests is None:
            all_doc_requests.extend(doc_requests)

    return all_doc_requests

def handle_hero(pattern):
    title = pattern['title']
    description = pattern['body_text']
    return [make_hero_title(title), make_hero_description(description), make_inline_image('https://www.gstatic.com/images/branding/product/1x/docs_64dp.png')]

def handle_matrix(pattern):
    title = pattern['matrix_items'][0]['title']
    # print('Matrix item1 title dump: {0}'.format(pattern['matrix_items'][0]['title']))
    return [make_matrix_children_title(title)]

def make_hero_title(text):
    text += "\n"
    global index
    text_length = len(text)
    prev_index = index + 4
    index += text_length

    end_index = prev_index + text_length

    print('end_index {0}'.format(end_index))

    return [
        {
            'insertText': {
                'location': {
                    'index': prev_index,
                },
                'text': text
            }
        }, {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': prev_index,
                    'endIndex': end_index
                },
                'paragraphStyle': {
                    'namedStyleType': 'TITLE'
                },
                'fields': 'namedStyleType'
            }
        }, {
            'updateTextStyle': {
                'range': {
                    'startIndex': prev_index,
                    'endIndex': end_index
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

def make_hero_description(text):
    text = text + "\n"
    global index
    text_length = len(text)
    prev_index = index + 4
    index += text_length

    end_index = prev_index + text_length

    print('end_index {0}'.format(end_index))

    return [
        {
            'insertText': {
                'location': {
                    'index': prev_index,
                },
                'text': text
            }
        }, {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': prev_index,
                    'endIndex': end_index
                },
                'paragraphStyle': {
                    'namedStyleType': 'HEADING_3'
                },
                'fields': 'namedStyleType'
            }
        }, {
            'updateTextStyle': {
                'range': {
                    'startIndex': prev_index,
                    'endIndex': end_index
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

def make_hero_table(text):
    text = text + "\n"
    global index
    text_length = len(text)
    prev_index = index + 4
    index += text_length

    end_index = prev_index + text_length

    print('end_index {0}'.format(end_index))

    return [
        {
            'insertText': {
                'location': {
                    'index': prev_index,
                },
                'text': text
            }
        }, {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': prev_index,
                    'endIndex': end_index
                },
                'paragraphStyle': {
                    'namedStyleType': 'HEADING_3'
                },
                'fields': 'namedStyleType'
            }
        }, {
            'updateTextStyle': {
                'range': {
                    'startIndex': prev_index,
                    'endIndex': end_index
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


def make_inline_image(url):
    global index
    img_length = 1
    prev_index = index + 4
    index += img_length

    end_index = prev_index + img_length

    print('end_index {0}'.format(end_index))

    return [ {
            'insertInlineImage': {
                'location': {
                    'index': prev_index
                },
                'uri':
                    url,
                'objectSize': {
                    'height': {
                        'magnitude': 250,
                        'unit': 'PT'
                    },
                    'width': {
                        'magnitude': 150,
                        'unit': 'PT'
                    }
                }
            }
        }
    ]


def make_matrix_children_title(text):
    text_length = len(text)
    return [
        {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': text
            }
        }, {
            'updateParagraphStyle': {
                'range': {
                    'startIndex': 1,
                    'endIndex': text_length
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
                    'endIndex': text_length
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
