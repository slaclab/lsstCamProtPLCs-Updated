[]#!/usr/bin/env python
# scripts/examples/simple_tcp_clie
# nt.py
import socket

from umodbus import conf
from umodbus.client import tcp

def gateway_write_read(add,value):
    message = tcp.write_multiple_registers(slave_id=config_id, starting_address=add, values=[value])
    response = tcp.send_message(message, sock)

    message = tcp.read_holding_registers(config_id,add,1)
    response = tcp.send_message(message, sock)

    if response[0] != value:
        raise ValueError("Value not writen!")

# Enable values to be signed (default is False).
conf.SIGNED_VALUES = False

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.1.100', 502))

config_id = 4

gateway_write_read(1,0x03)
gateway_write_read(2,0x00)

gateway_write_read(5,0x01)
gateway_write_read(6,0x02)
gateway_write_read(7,0x03)
gateway_write_read(8,0x04)
gateway_write_read(9,0x05)
gateway_write_read(10,0x06)
gateway_write_read(11,0x07)
gateway_write_read(12,0x08)
gateway_write_read(13,0x09)
gateway_write_read(14,0x0A)
gateway_write_read(15,0x0B)
gateway_write_read(16,0x0C)
gateway_write_read(17,0x0D)
gateway_write_read(18,0x0E)
gateway_write_read(19,0x0F)


message = tcp.read_holding_registers(36, 82, 1)
response = tcp.send_message(message, sock)
print(response)

for add in range(20,37):
    gateway_write_read(add, 0x00)

gateway_write_read(37,99)
gateway_write_read(41,0x00)

print ("Done")



sock.close()


