#!.env/bin/python3
import threading
from controller import Monitor
from webserver.server import MyServer, webServer
from http.server import HTTPServer
from utils import commit_errors



if __name__ == "__main__":        
    monitor_server = Monitor()
    
    th_monitor = threading.Thread(target=monitor_server.monitoring_daemon, daemon=True)
    th_monitor.start()

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        commit_errors(KeyboardInterrupt, __file__)
    except Exception as err:
        commit_errors(err, __file__)

    webServer.server_close()
    print("Server stopped.")
