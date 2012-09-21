# Cisco/Scientific-Atlanta/WebStar DPC2100 cable modem
"""
name: Cisco/Scientific-Atlanta/WebStar DPC2100 cable modem
hardware version: 2.1
software version: dpc2100rx-v202r1256-110531Uas-TWC

I HATE MY ISP.
"""

import requests

def set_admin_mode():
    """ Access levels:
           1 - locked down, default
           2 - seems to unlock (all) things
           3 - unlock all things
    """
    url = "http://192.168.100.1/goform/_aslvl"
    data = {
           "SAAccessLevel": "2",
           "SAUsername": "admin",
           "SAPassword": "W2402",
           }
    response = requests.post(url, data=data)
    print "status: " + str(response.status_code)
    print response.text
    return response

def power_cycle():
    """ Reboot the modem.
    """
    response = requests.post("http://192.168.100.1/goform/gscan", data={"SADownStartingFrequency": "54900000"})
    print "status: " + str(response.status_code)
    print response.text
    return response

def factory_reset():
    """
    Reset all cable modem parameters to factory default settings. This should
    also reboot the machine.

    see: http://192.168.100.1/reset.asp
    """
    data = {
            "ResetToFactory": "3",
            "RestoreFactoryYes": "1",
           }
    response = requests.post("http://192.168.100.1/goform/reset", data=data)
    print "status: " + str(response.status_code)
    print response.text
    return response

def set_firmware():
    raise NotImplementedError

    data = {}
    response = requests.post("http://192.168.100.1/goform/_swdld", data=data)
    print "status: " + str(response.status_code)
    print response.text
    return response

if __name__ == "__main__":
    set_admin_mode()
