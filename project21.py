# Python Automation
import os
import requests
import schedule
import time
from dotenv import load_dotenv

load_dotenv()
mobile_number = os.getenv("mobile_number")


def send_message():
    resp = requests.post('https://textbelt.com/text', {
         "phone": mobile_number,
         "message": "Good Morning Boss..Are u ready to fight!!!...",
         "key": "textbelt"         
    })
    print(resp.json())
    
    
#schedule.every().day.at("06:00").do(send_message)
schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)


    
    
    