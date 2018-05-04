from umodbus import conf
from umodbus.client import tcp
import socket
import time



class PlutoGateway():

    def __init__(self, ip , port):
        # Enable values to be signed (default is False).
        conf.SIGNED_VALUES = False

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))




    def gateway_config_write_read(self,add, value):
        config_id = 4

        message = tcp.write_multiple_registers(slave_id=config_id, starting_address=add, values=[value])
        response = tcp.send_message(message, self.sock)

        print(".")
        time.sleep(0.1)

        message = tcp.read_holding_registers(config_id, add, 1)
        response = tcp.send_message(message, self.sock)

        if response[0] != value:
            raise ValueError("Value not writen!")

    def close(self):
        self.sock.close()

plutoGateway = PlutoGateway('192.168.1.100', 502)


# Reset all registers to 0
for add in range(0,41+1):
    plutoGateway.gateway_config_write_read(add, 0x00)

# Activate Data to Pluto Area 0, 1
plutoGateway.gateway_config_write_read(1,0b011)

# Data to Pluto Timeout = 1000 ms
plutoGateway.gateway_config_write_read(2,1000)

# Additional Data Areas for PLC 0
plutoGateway.gateway_config_write_read(5,0x01)
plutoGateway.gateway_config_write_read(6,0x02)
plutoGateway.gateway_config_write_read(7,0x03)
plutoGateway.gateway_config_write_read(8,0x04)
plutoGateway.gateway_config_write_read(9,0x05)
plutoGateway.gateway_config_write_read(10,0x06)
plutoGateway.gateway_config_write_read(11,0x07)
plutoGateway.gateway_config_write_read(12,0x08)
plutoGateway.gateway_config_write_read(13,0x09)
plutoGateway.gateway_config_write_read(14,0x0A)
plutoGateway.gateway_config_write_read(15,0x0B)
plutoGateway.gateway_config_write_read(16,0x0C)
plutoGateway.gateway_config_write_read(17,0x0D)
plutoGateway.gateway_config_write_read(18,0x0E)
plutoGateway.gateway_config_write_read(19,0x0F)
plutoGateway.gateway_config_write_read(20,0x10)
plutoGateway.gateway_config_write_read(21,0x11)
plutoGateway.gateway_config_write_read(22,0x12)


print ("Done")

plutoGateway.close()



