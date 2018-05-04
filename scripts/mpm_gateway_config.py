from .plutoGateway import PlutoGateway

plutoGateway = PlutoGateway('192.168.1.100', 502)


# Reset all registers to 0
for add in range(0,41+1):
    plutoGateway.gateway_config_write_read(add, 0x00)

# Activate Data to Pluto Area 0, 1 and 2
plutoGateway.gateway_config_write_read(1,0b0111)

# Data to Pluto Timeout = 1000 ms
plutoGateway.gateway_config_write_read(2,1000)

# Additional Data Areas for PLC 1
plutoGateway.gateway_config_write_read(5,0x11)
plutoGateway.gateway_config_write_read(6,0x12)
plutoGateway.gateway_config_write_read(7,0x13)
plutoGateway.gateway_config_write_read(8,0x14)
plutoGateway.gateway_config_write_read(9,0x00)
plutoGateway.gateway_config_write_read(10,0x00)
plutoGateway.gateway_config_write_read(11,0x00)
plutoGateway.gateway_config_write_read(12,0x00)
plutoGateway.gateway_config_write_read(13,0x00)
plutoGateway.gateway_config_write_read(14,0x00)

# Additional Data Areas for PLC 2
plutoGateway.gateway_config_write_read(15,0x21)
plutoGateway.gateway_config_write_read(16,0x22)
plutoGateway.gateway_config_write_read(17,0x23)
plutoGateway.gateway_config_write_read(18,0x24)
plutoGateway.gateway_config_write_read(19,0x25)
plutoGateway.gateway_config_write_read(20,0x26)
plutoGateway.gateway_config_write_read(21,0x27)
plutoGateway.gateway_config_write_read(22,0x28)
plutoGateway.gateway_config_write_read(23,0x00)
plutoGateway.gateway_config_write_read(24,0x00)


# Additional Data Areas for PLC 3
plutoGateway.gateway_config_write_read(25,0x31)
plutoGateway.gateway_config_write_read(26,0x32)
plutoGateway.gateway_config_write_read(27,0x33)
plutoGateway.gateway_config_write_read(28,0x34)
plutoGateway.gateway_config_write_read(29,0x35)
plutoGateway.gateway_config_write_read(30,0x36)
plutoGateway.gateway_config_write_read(31,0x37)
plutoGateway.gateway_config_write_read(32,0x38)
plutoGateway.gateway_config_write_read(33,0x39)
plutoGateway.gateway_config_write_read(34,0x00)

# Data to Pluto Cycle time = 100 ms
plutoGateway.gateway_config_write_read(37,100)

# Gateway Node number = 0
plutoGateway.gateway_config_write_read(41,0x001)


print ("Done")



plutoGateway.close()


