import threading
from leads.controller import Monitor
from leads.models import Leads
from whatsapp.seln import AutomationWhatsApp

def init():
    _leads = Leads.objects.all().order_by('city').values_list()

    list_cities = list(_leads)
    _cities, _numbers = list(), list()

    for i in range(len(list_cities)):
        _cities.append(list_cities[i][2]) 
        _numbers.append(list_cities[i][1]) 

    try:
        th_monitor = threading.Thread(target=Monitor(cities=_leads).monitoring_daemon, daemon=True, args=(_leads, ))
        th_monitor.start()
        
        th_sender = AutomationWhatsApp(leads=_cities, number=_numbers)
        threading.Thread(target=th_sender.send_status, daemon=True).start()
    except KeyboardInterrupt:
        print('KeyboardInterrupt', __file__)
    except Exception as err:
        print(err, __file__)