from flask import Flask
import socket
import json

app = Flask(__name__)


@app.route("/add_to_calendar/<string:year>/<string:month>/<string:day>/<string:hour>/<string:minute>/<string:event>")
def add_to_calendar(year: str, month: str, day: str, hour: str, minute: str, event: str):
    """
    Add event to calendar
    :param year: (str) year of event
    :param month: (str) month of event
    :param day: (str) day of event
    :param hour: (str) time (hour) of event
    :param minute: (str) time (minute) of event
    :param event: (str) description of event
    :return: None
    """
    # TODO: backend calendar object add event


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
