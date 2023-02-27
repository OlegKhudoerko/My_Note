from datetime import datetime

import json_model


class Notes:
    id = 0
    title = ''
    msg = ''
    change_date = None

    def __init__(self, title, msg):

        self.id = Notes.id + 1
        Notes.id += 1
        self.title = title
        self.msg = msg
        self.change_date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    def __str__(self):
        details = ''
        details += f'{self.id} '
        details += f'{self.title}; '
        details += f'{self.msg}; '
        details += f'{self.change_date}'
        return details

    def get_id(self):
        self.id = len(json_model.load_file()) + 1
        return self.id

    def get_title(self):
        return self.title

    def get_msg(self):
        return self.msg

    def get_change_date(self):
        return self.change_date

    def set_id(self, data):
        self.id = data
        return self.id

    def set_title(self, x):
        self.title = x

    def set_msg(self, x):
        self.msg = x

    def set_change_date(self, x):
        self.change_date = x
