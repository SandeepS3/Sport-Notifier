import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dataclasses import dataclass

'''
    Message Types
'''
@dataclass
class Email:
    to: str
    subject: str
    body: str
    is_HTML: bool = False

@dataclass
class SMS:
    number: str
    gateway: str
    subject: str
    body: str
    @property
    def recipient(self) -> str:
        return self.number + self.gateway


'''
    Messager
'''
@dataclass
class Messenger:
    username: str # ALSO THE FROM ADDRESS
    password: str
    conn: smtplib.SMTP = None

    def open_conn(self):
        # CREATE CONNECTION TO SMTP SERVICE
        self.conn = smtplib.SMTP("smtp.gmail.com",587)
        #self.conn = smtplib.SMTP("smtp-mail.outlook.com",587)
        self.conn.ehlo()
        self.conn.starttls()
        self.conn.ehlo
        self.conn.login(self.username, self.password)

    def close_conn(self):
        # CLOSE CONNECTION TO SMTP SERVICE
        self.conn.close()

    def send_sms(self, msg, one_time=False):
        if one_time:
            self.open_conn()

        # CREATE MESSAGE
        message = MIMEMultipart("alternative")
        message["From"] = self.username
        message["To"] =  msg.recipient
        message["Subject"] = msg.subject
        message.attach(MIMEText(msg.body, "plain"))
        # SEND MESSAGE
        self.conn.sendmail(self.username, msg.recipient, message.as_string())

        if one_time:
            self.close_conn()

    def send_email(self, msg, one_time=False):
        if one_time:
            self.open_conn()

        # CREATE MESSAGE
        message = MIMEMultipart("alternative")
        message["From"] = self.username
        message["To"] = msg.to
        message["Subject"] = msg.subject
        if msg.is_HTML:
            message.attach(MIMEText(msg.body, "html"))
        else:
            message.attach(MIMEText(msg.body, "plain"))
        # SEND MESSAGE
        self.conn.sendmail(self.username, msg.to, message.as_string())

        if one_time:
            self.close_conn()
