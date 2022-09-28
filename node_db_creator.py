import os
import subprocess
import re


def get_avail_partitions():
    # cmd1 = "sinfo"
    # ret = subprocess.run(cmd1, capture_output=True, shell=True)
    cmd2 = "sacctmgr list associations where user=$USER format=User,MaxJobs,Partition,GrpCPUs"
    ret = subprocess.run(cmd2, capture_output=True, shell=True)
    # print(ret.stdout.decode())
    node_list_info = (ret.stdout.decode().split('\n'))
    sep = re.compile('[\s]+')
    partitions = []
    for line in node_list_info:
        part_values = ([x for x in sep.split(line) if len(x) > 1])
        if len(part_values) > 0:
            partitions.append(part_values[-2])  # split only the the partition name column

    partitions = partitions[2:]  # remove the header
    # print(partitions)
    return partitions


def get_avail_nodes(partitions):
    output = set()
    cmd1 = "sinfo"
    ret = subprocess.run(cmd1, capture_output=True, shell=True)
    raw_data = ret.stdout.decode()
    y = [x for x in raw_data.split('\n')[1:] if len(x) > 0]
    avail_part = [node.split() for node in y if (node.split())[0].replace('*', '') in partitions]
    print(avail_part)
    for avail_node in avail_part:
        nodes = avail_node[-1]
        if '[' in nodes:
            for nums in (nodes.split("[")[1][:-1]).split(','):  # Need to split the array"
                zero_pad = len(nums.split("-")[0])
                if "-" in nums:
                    for num in range(int(nums.split("-")[0]), int(nums.split("-")[1]) + 1):
                        output.add("node" + str(num).zfill(zero_pad))
                else:
                    output.add("node" + str(nums))

    return (sorted(output))


if __name__ == "__main__":
    print(get_avail_nodes(get_avail_partitions()))
