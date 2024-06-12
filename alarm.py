import time
import requests
import pytz

from datetime import datetime

send_times = ["7:30", "12:00", "13:00", "17:45", "15:38", "15:39"]
while True:
    current_time = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime("%H:%M")

    if current_time in send_times:
        ct_to_seconds = int(current_time.split(":")[0]) * 60 + int(current_time.split(":")[1]) * 60

        index = send_times.index(current_time)
        next_time = send_times[index + 1] if index + 1 < len(send_times) else send_times[0]
        nt_to_seconds = int(next_time.split(":")[0]) * 60 + int(next_time.split(":")[1]) * 60

        requests.post("http://localhost:8000/messages/send")
        sleep_time = abs(nt_to_seconds - ct_to_seconds)
        time.sleep(sleep_time)