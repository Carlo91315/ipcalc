
def ip2dec(ip):
    ip = str(ip).split(".")
    ip1 = int(ip[0]) << 24
    ip2 = int(ip[1]) << 16
    ip3 = int(ip[2]) << 8
    ip4 = int(ip[3]) 
    return ip1 + ip2 + ip3 + ip4

def dec2ip(ip):
    ip1 = ip >> 24 & 255
    ip2 = ip >> 16 & 255
    ip3 = ip >> 8 & 255
    ip4 = ip & 255
    return "%s.%s.%s.%s" % (ip1, ip2, ip3, ip4)

def cidr2mask(mask):
    mask = (1 << 32) - (1 << 32 - mask)
    return dec2ip(mask) 

dec_ip = ip2dec("192.168.0.2")
dec_mask = ip2dec(cidr2mask(24))

size = ((1 << 32) - dec_mask - 1).bit_length()
cidr = 32 - size
network = dec_ip & dec_mask
broadcast = network + (1 << size) - 1


print("IP %s" % (dec2ip(dec_ip)))
print("MASK %s" % (dec2ip(dec_mask)))
print("NET %s" % (dec2ip(network)))
print("CIDR %s" % (cidr))
print("Broadcast %s" % (dec2ip(broadcast)))
