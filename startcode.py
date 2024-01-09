# Script to send notifications about soccer scores
import os
from dotenv import load_dotenv

load_dotenv()
import requests
import json

xsportkey = os.environ.get("xsportkey")
rapidapikey = os.environ.get("rapidapikey")


def startrun():
    # Setting up API 1 (API Sports Football)
    url1 = "https://v3.football.api-sports.io/{endpoint}"
    header1 = {"x-apisports-key": xsportkey}

    # Setting up API 2 (Rapid API Football)
    url = "https://football98.p.rapidapi.com/competitions"
    headers = {
        "X-RapidAPI-Key": rapidapikey,
        "X-RapidAPI-Host": "football98.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)


startrun()
