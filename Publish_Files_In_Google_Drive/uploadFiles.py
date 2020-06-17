from __future__ import print_function
import os
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload
import pandas as pd
import sys

def upload_files():
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None

    try:
        os.remove("fileIds.csv")
        print('Arquivo fileIds removido com sucesso!')
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print('Arquivo fileIds não encontrado!')     
    SCOPES = 'PATH/drive.file'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(
            'client_secret.json', scope=SCOPES)
        creds = tools.run_flow(flow, store,flags) \
                if flags else tools.run(flow,store)
    DRIVE = build('drive', 'v3', http = creds.authorize(Http()))

    FILES = (
        ('YOUR_FILE.csv','(application/vnd.ms-excel)'),
        ('YOUR_FILE.xlsx','(application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)'),
        ('YOUR_FILE.xlsx','(application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)'),
        ('YOUR_FILE.xlsx','(application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)'),
    )

    folder_id = 'YOUR FOLDER ID'
    filesIds = []
    for filename, mimeType in FILES:
        metadata = {'name': filename,
                    'parents': [folder_id],
                    'resumable':True,}               
        if mimeType:
            metadata['mimeType'] = mimeType
        res = DRIVE.files().create(body=metadata, media_body=filename).execute()
        filesIds.append(res.get('id'))


        if res:
            print('Upload "%s" (%s): ' %(filename,res['mimeType']))  
            print('File ID: %s' %(res.get('id')))

    df = pd.DataFrame(filesIds)
    df.to_csv('fileIds.csv', sep=';', index=False, header=None)