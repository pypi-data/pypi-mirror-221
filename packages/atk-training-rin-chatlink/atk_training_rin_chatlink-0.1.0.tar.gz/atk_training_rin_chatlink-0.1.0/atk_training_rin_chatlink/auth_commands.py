from __future__ import print_function
import os

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/chat.spaces.readonly",
          "https://www.googleapis.com/auth/chat.messages.readonly"]


def connect_to_app():
    flow = InstalledAppFlow.from_client_secrets_file(
        os.path.dirname(__file__)+'/client_secrets.json', SCOPES)
    creds = flow.run_local_server()
    service = build('chat', 'v1', credentials=creds)
    return service


class ChatApp:
    def __init__(self, target: str):
        self.target_space = target
        self.service = connect_to_app()
        self.space_rsc_name = self.get_target_space()

    def get_target_space(self):
        get_spaces = self.service.spaces().list().execute()
        space_resource_name = [spc.get("name") for spc in get_spaces.get('spaces') if
                               spc.get('displayName') == self.target_space]
        return space_resource_name[0]

    def get_messages(self):
        raw_messages = self.service.spaces().messages().list(parent=self.space_rsc_name, pageSize=1000).execute()
        msg_only = raw_messages.get('messages')
        msg_list = []
        for i, x in enumerate(msg_only):
            try:
                split_msg = x.get('text').split('\n')
                msg_list.extend(split_msg)
            except AttributeError:  # deleted message?
                continue
        return msg_list
