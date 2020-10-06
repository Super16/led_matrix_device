try:
    import usocket as socket
except:
    import socket

import network


SSID = 'ESP32'
PASSWORD = '123456789'

# start access point
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=SSID, authmode=network.AUTH_WPA_WPA2_PSK, password=PASSWORD)

while ap.active() == False:
    pass

def web_page():
    """webpage to response at 192.168.4.1"""
    html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
    <body><h1>LED Matrix Device Test Page</h1></body></html>"""
    return html

# Socket settings
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    request = conn.recv(1024)
    response = web_page()
    conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    conn.send(response)
    conn.close()