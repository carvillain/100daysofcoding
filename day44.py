import ipaddress

def ip_to_num(ip):
    num = int(ipaddress.ip_address(ip))
    return num
    


def num_to_ip(num):
    ip =  str(ipaddress.ip_address(num))
    return ip