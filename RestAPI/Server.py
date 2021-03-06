from flask import Flask
import socket
import json

from Model.Command import Command
from Model.RequestHandler import RequestHandler
from Util.WR_Util import *

app = Flask(__name__)
requestHandler = RequestHandler()


@app.route("/add_to_calendar/<string:command>/<string:args>")
def add_to_calendar(command: Command, args: str):
    """
    Add event to calendar
    :param command: (str) command of event
    :param args: (str) arguments for RequestHandler
    :return: None
    """
    requestHandler.handle_event_text(command, args)


def getHost():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        print("Could not find ip address.")
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP


def updateHost(ip_addr: str):
    with open("./server_ip_address.json", "w") as file:
        json.dump({"address": ip_addr}, file)


if __name__ == "__main__":
    ip = getHost()
    updateHost(ip)
    app.run(host=ip, port=8000)
