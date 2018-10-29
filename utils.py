'''
    Utils library for tel file generation
'''

def convert_ip_to_mac(ip):
    updated_ip = []
    for i in ip.split("."):
        if len(i) == 3:
            updated_ip.append(i)
        elif len(i) == 2:
            updated_ip.append("0" + i)
        else:
            updated_ip.append("00" + i)

    ip_addr = "".join(updated_ip)
    return ip_addr[:4] + "." + ip_addr[4:8] + "." + ip_addr[8:]

def ip_normalizer(octet):
    if len((octet)) == 1:
        noctet = "00" + octet
    elif len((octet)) == 2:
        noctet = "0" + octet
    elif len((octet)) == 3:
        noctet = octet
    return noctet