from __future__ import print_function
import os
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import csv


def delete_file():
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None

    SCOPES = 'PATH/drive.file'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(
            'client_secret.json', scope=SCOPES)
        creds = tools.run_flow(flow, store,flags) \
                if flags else tools.run(flow,store)
    DRIVE = build('drive', 'v3', http = creds.authorize(Http()))
  

    results = []
    with open("fileIds.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter = ';') # change contents to floats
        for row in reader: # each row is a list
            results.append(row[0])

    for file_id in results:
        res = DRIVE.files().delete(fileId = file_id).execute()
        print(res.get('id'))
