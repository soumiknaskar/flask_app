from datetime import datetime


class Entries():
    def __init__(self, title = None, text = None):
        self.title = title
        self.text = text
        self.created_at = datetime.utcnow()

    def user(self):
        return self.title, self.text, self.created_at

    def __repr__(self):
        return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)