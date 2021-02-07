import threading
from leads.controller import Monitor
from leads.models import Leads
from whatsapp.seln import AutomationWhatsApp

def init():
    try:
        th_monitor = threading.Thread(target=Monitor().monitoring_daemon, daemon=True)
        th_monitor.start()
    except KeyboardInterrupt:
        print('KeyboardInterrupt', __file__)
    except Exception as err:
        print(err, __file__)