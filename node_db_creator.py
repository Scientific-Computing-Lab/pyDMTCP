import os
import subprocess
import re


def get_avail_partitions():
    cmd1 = "sinfo"
    ret = subprocess.run(cmd1, capture_output=True, shell=True)
    cmd2 = "sacctmgr list associations where user=$USER format=User,MaxJobs,Partition,GrpCPUs"
    ret = subprocess.run(cmd2, capture_output=True, shell=True)
    # print(ret.stdout.decode())
    node_list_info = (ret.stdout.decode().split('\n'))
    sep = re.compile('[\s]+')
    partitions = []
    for line in node_list_info:
        part_values = ([x for x in sep.split(line) if len(x) > 1])
        if len(part_values) > 0:
            partitions.append(part_values[-2])

    partitions = partitions[2:]  # remove the header
    return partitions

def get_avail_nodes():
    cmd =


get_avail_partitions()
