from seln import AutomationWhatsApp
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--city", help="type the city")
(options, args) = parser.parse_args()


if __name__ == '__main__':
    zp_instance = AutomationWhatsApp().scan_qr_code()
    while True:
        pass