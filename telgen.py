''''
    Sapro Config generator tool

'''

from utils import convert_ip_to_mac
from utils import ip_normalizer

with open('/Users/vijshekh/PycharmProjects/sapros/18.20.40.2.tel', "r") as f:
    lines = f.readlines()
svariable = raw_input       ("Enter s-variable in format X or XX or XXX : ")
evariable = raw_input       ("Enter e-variable in format X or XX or XXX : ")
sapro_ip_range = raw_input  ("Enter Sapro IP range in format x.x.x      : ")
sapro_ip_split = sapro_ip_range.split(".")
sapro_first_octect = sapro_ip_split[0]
sapro_second_octect = sapro_ip_split[1]
sapro_third_octect = sapro_ip_split[2]
print                       ("sapro_first_octect                        : %s" %sapro_first_octect)
print                       ("sapro_second_octect                       : %s" %sapro_second_octect)
print                       ("sapro_third_octect                        : %s" %sapro_third_octect)

if len((sapro_first_octect)) > 4:
    exit(0)

sapro_first_octect_normalized = ip_normalizer(sapro_first_octect)
sapro_second_octect_normalized = ip_normalizer(sapro_second_octect)
sapro_third_octect_normalized = ip_normalizer(sapro_third_octect)

print                       ("sapro_first_octect_normalized             : %s" %sapro_first_octect_normalized)
print                       ("sapro_second_octect_normalized            : %s" %sapro_second_octect_normalized)
print                       ("sapro_third_octect_normalized             : %s" %sapro_third_octect_normalized)

for i in range(int(svariable), int(evariable)):
    variable = str(i)
    digits = [int(x) for x in str(variable)]
    print digits
    client_addr = sapro_second_octect + "." + sapro_third_octect + "." + variable
    client_macf = convert_ip_to_mac(client_addr)
    client_vlan = sapro_third_octect + variable
    client_vlan = client_vlan[0:4]
    sapro_ip = sapro_ip_range + "." + variable
    sapro_loppback_ip = client_addr + ".1"
    sapro_mac = convert_ip_to_mac(sapro_ip)
    out_file = "{}.tel".format(sapro_ip)
    print "CLIENT MAC         == " + client_macf
    print "CLIENT ADDR        == " + client_addr
    print "CLIENT VLAN        == " + client_vlan
    print "SAPRO INSTANCE IP  == " + sapro_ip
    print "SAPRO INSTANCE Lo0 IP == " + sapro_loppback_ip
    print "SAPRO INSTANCE MAC    == " + sapro_mac
    print ("Generating files based on input variable : " + variable)
    w = open(out_file, 'w')
    for l in lines:
        lnew = l.replace('0200.4000.2', client_macf).replace('20.40.2', client_addr).replace('2002', client_vlan)\
            .replace('18.20.40.2',sapro_ip).replace('0180.2004.002', sapro_mac).replace('20.40.2.1', sapro_loppback_ip)
        w.write(lnew)
    print "++++ DONE One file ++++"