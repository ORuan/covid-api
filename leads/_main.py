import threading
from leads.controller import Monitor
from leads.models import Leads
from whatsapp.seln import AutomationWhatsApp
import logging

def init():
    try:
        th_monitor = threading.Thread(target=Monitor().monitoring_daemon, daemon=True)
        th_monitor.start()
    except KeyboardInterrupt:
        logging.error(err)
    except Exception as err:
        print('KeyboardInterrupt', __file__)
