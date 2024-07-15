import requests
import schedule
import time

def send_signal():
    response = requests.post("http://localhost:8000/messages/send")
    print(f"Status Code: {response.status_code}, Response: {response.text}")

schedule.every(1).minutes.do(send_signal)

while True:
    schedule.run_pending()
    time.sleep(1)