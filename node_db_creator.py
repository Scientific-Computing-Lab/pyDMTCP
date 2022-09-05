import os
import subprocess
import re


def get_node_list():
    cmd = "sinfo"
    ret = subprocess.run(cmd, capture_output=True, shell=True)
    node_list_info = (ret.stdout.decode().split('\n'))
    sep = re.compile('[\s]+')
    for line in node_list_info:
        # print(line)
        print(sep.split(line))
        print(line.split(' ')[-1])


get_node_list()
