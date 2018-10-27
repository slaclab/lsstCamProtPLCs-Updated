#
# MPM Pluto Gateway configuration script
#
# SLAC National Accelerator Laboratory
# Joao Rodrigues (joaoprod@slac.stanford.edu)
#

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

        time.sleep(0.1)

        message = tcp.read_holding_registers(config_id, add, 1)
        response = tcp.send_message(message, self.sock)

        print("..")

        if response[0] != value:
            raise ValueError("Value not writen!")

    def close(self):
        self.sock.close()



plutoGateway = PlutoGateway('192.168.1.132', 502)


# Reset all registers to 0
for add in range(0,41+1):
    plutoGateway.gateway_config_write_read(add, 0x00)

# Activate Data to Pluto Area 0, 1 and 2
plutoGateway.gateway_config_write_read(1,0b0111)

# Data to Pluto Timeout = 0 
plutoGateway.gateway_config_write_read(2,0)

# Additional Data Areas for PLC 1
plutoGateway.gateway_config_write_read(5,0x0101)
plutoGateway.gateway_config_write_read(6,0x0102)
plutoGateway.gateway_config_write_read(7,0x0103)
plutoGateway.gateway_config_write_read(8,0x0104)
plutoGateway.gateway_config_write_read(9,0x0000)
plutoGateway.gateway_config_write_read(10,0x0000)
plutoGateway.gateway_config_write_read(11,0x0000)
plutoGateway.gateway_config_write_read(12,0x0000)
plutoGateway.gateway_config_write_read(13,0x0000)
plutoGateway.gateway_config_write_read(14,0x0164)

# Additional Data Areas for PLC 2
plutoGateway.gateway_config_write_read(15,0x0201)
plutoGateway.gateway_config_write_read(16,0x0202)
plutoGateway.gateway_config_write_read(17,0x0203)
plutoGateway.gateway_config_write_read(18,0x0204)
plutoGateway.gateway_config_write_read(19,0x0205)
plutoGateway.gateway_config_write_read(20,0x0206)
plutoGateway.gateway_config_write_read(21,0x0207)
plutoGateway.gateway_config_write_read(22,0x0208)
plutoGateway.gateway_config_write_read(23,0x0000)
plutoGateway.gateway_config_write_read(24,0x0264)


# Additional Data Areas for PLC 3
plutoGateway.gateway_config_write_read(25,0x0301)
plutoGateway.gateway_config_write_read(26,0x0302)
plutoGateway.gateway_config_write_read(27,0x0303)
plutoGateway.gateway_config_write_read(28,0x0304)
plutoGateway.gateway_config_write_read(29,0x0305)
plutoGateway.gateway_config_write_read(30,0x0306)
plutoGateway.gateway_config_write_read(31,0x0307)
plutoGateway.gateway_config_write_read(32,0x0308)
plutoGateway.gateway_config_write_read(33,0x0309)
plutoGateway.gateway_config_write_read(34,0x0364)


# Data to Pluto Cycle time = 100 ms
plutoGateway.gateway_config_write_read(37,100)

# Gateway Node number = 0
plutoGateway.gateway_config_write_read(41,0x001)


print ("Done")

plutoGateway.close()


