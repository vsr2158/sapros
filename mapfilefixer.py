import os
import re

orig_ip = '1.1.1.1'

with open('SW_3850_3.map', "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if "Name" in lines[i]:
            line_item = lines[i]
            orig_ip=lines[i].split("=")[1].replace("\n",'').replace('\"','').replace(" ", '')
            tokens = lines[i+25].split("/")
            tokens[7]=orig_ip+".tel\"\n"
            lines[i+25] = "/".join(tokens)

with open("SW-3850-20.map", "w") as fh:
    fh.writelines(lines)

