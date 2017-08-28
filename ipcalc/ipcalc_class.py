


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

class Network():
    def __init__(self):
        self.ip = ip2dec('192.168.0.1')
        self.mask = ip2dec('255.255.255.0')

    def set_ip(self, ip):
        self.ip = ip2dec(ip)

    def set_mask(self, mask):
        self.mask = ip2dec(mask)

    def set_bits(self, bit):
        self.mask = ip2dec(cidr2mask(bit))

    def get_network(self):
        network = self.ip & self.mask
        return dec2ip(network)

    def get_ip(self):
        return dec2ip(self.ip)

    def get_mask(self):
        return dec2ip(self.mask)

    def get_broadcast(self):
        size = ((1 << 32) - self.mask - 1).bit_length()
        network = self.ip & self.mask
        return dec2ip(network + (1 << size) - 1)

    def get_bits(self):
        size = ((1 << 32) - self.mask - 1).bit_length()
        return 32 - size

network = Network()
network.set_ip('196.25.1.1')
network.set_mask('255.255.255.0')
print network.get_network()
print network.get_broadcast()
print network.get_bits()
network.set_mask('255.255.255.128')
print network.get_bits()
print network.get_broadcast()

network2 = Network()
network2.set_ip('196.25.1.1')
network2.set_mask('255.255.255.0')
print network2.get_bits()
print network2.get_broadcast()
