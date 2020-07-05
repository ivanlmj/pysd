from apscheduler.schedulers.background import BackgroundScheduler
import requests
from bs4 import BeautifulSoup
from app import app

def check_dead():
    services = list()
    uri = "http://" + app.config['SERVER_NAME'] + "/dead"
    r = requests.get(uri)
    if r.status_code == 200:
        html = BeautifulSoup(r.content, 'html.parser')
        for li in html.select('li'):
            service = li.text.split(':')[0].strip()
            if service in app.config['CORE_SERVICES']:
                services.append(service)
    if len(services) != 0:
        print("Core Services (out-of-service):", services)


sched = BackgroundScheduler(daemon=True)
sched.add_job(check_dead, 'interval', seconds=60)
sched.start()
