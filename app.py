# -*- coding: utf-8 -*-

# Sample Python code for youtube.liveChatMessages.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os, datetime

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


#-----------------------------------------------------------------------------------------
from flask import Flask
app = Flask(__name__)

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "client_secret.json"

# Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)
#-----------------------------------------------------------------------------------------
channel_id=""

def get_channel_id():
    request = youtube.channels().list(
        part="id",
        mine=True
    )
    response = request.execute()
    id=response['items'][0]['id']
    return(id)

def get_current_livechat_id():
    request = youtube.liveBroadcasts().list(
        part="snippet,contentDetails,status",
        broadcastType="all",
        mine=True
    )
    response = request.execute()
    live_id = response['items'][0]['liveChatId']
    return(live_id)

def get_latest_message():
    pass

def get_message_list():
    pass

def get_poll_results():
    pass

#-----------------------------------------------------------------------------------------

@app.route('/')
def hello():
    return(get_current_livechat_id())


if __name__ == "__main__":
    channel_id=str(get_channel_id())
    app.run()