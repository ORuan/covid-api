#!.env/bin/python3
import threading
from controller import Monitor
from utils import commit_errors
from whatsapp.seln import AutomationWhatsApp


if __name__ == "__main__":        
    monitor_server = Monitor()
    server_whatsapp = AutomationWhatsApp()
    try:
        th_monitor = threading.Thread(target=monitor_server.monitoring_daemon, daemon=True)
        th_monitor.start()

        th_send = threading.Thread(target=server_whatsapp.send_status, daemon=True)
        th_send.start()
        while True:
            pass
    except KeyboardInterrupt:
        commit_errors(KeyboardInterrupt, __file__)
    except Exception as err:
        commit_errors(err, __file__)

    print("Server stopped.")
