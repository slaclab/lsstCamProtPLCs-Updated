from umodbus import conf
from umodbus.client import tcp
import socket
import time



class PlutoGateway():

    def __init__(self, ip , port):
        # Enable values to be signed (default is False).
        conf.SIGNED_VALUES = False

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(ip, port)




    def gateway_config_write_read(self,add, value):
        config_id = 4

        message = tcp.write_multiple_registers(slave_id=config_id, starting_address=add, values=[value])
        response = tcp.send_message(message, self.sock)

        time.sleep(0.1)

        message = tcp.read_holding_registers(config_id, add, 1)
        response = tcp.send_message(message, self.sock)

        if response[0] != value:
            raise ValueError("Value not writen!")

    def close(self):
        self.sock.close()