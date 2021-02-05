import threading
from leads.controller import Monitor
from leads.models import Leads


def init():
    leads = Leads.objects.all().order_by('city').values_list()
    try:
        th_monitor = threading.Thread(target=Monitor(cities=leads).monitoring_daemon, daemon=True, args=(leads, ))
        th_monitor.start()
        
    except KeyboardInterrupt:
        print('KeyboardInterrupt', __file__)
    except Exception as err:
        print(err, __file__)