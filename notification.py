from datetime import datetime

class Notification:
    def __init__(self, message):
        self.message = message
        self.created_at = datetime.now()
    def send(self):
        pass
    def __str__(self):
        return f"{self.message} - {self.created_at}"

class Email(Notification):
    def send(self):
        print(f"email gönderildi: {self.message}")

class Sms(Notification):
    def send(self):
        print(f"sms gönderildi: {self.message}")

class Push(Notification):
    def send(self):
        print(f"push bildirimi gönderildi : {self.message}")