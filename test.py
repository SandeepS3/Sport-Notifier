import os
import requests
from PyMessenger import Email, SMS, Messenger

# Load environment variables from .env file
from dotenv import load_dotenv

load_dotenv()

url = "https://www.boredapi.com/api/activity"
rsp = requests.request("GET", url).json()
# print(rsp)
# print(rsp["activity"])
password = os.environ.get("passowrd")
# Sending the Text
my_messenger = Messenger("deep.testscript", password)

number = "2019276063"
gateway = "@vtext.com"
subject = ""
body = "Testing Testing 123 :)\n"
msg = SMS(number, gateway, subject, body)

my_messenger.send_sms(msg, one_time=True)
print("done")
