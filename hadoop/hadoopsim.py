#!/usr/bin/python3

import argparse
import typing
import random
import sys
import subprocess

TMP_FILE = "/tmp/hadoop"

class Node_Data:

    def __init__(self) -> None:
        self.data = []

    def add_line(self, line : str) -> None:
        if len(line.strip()) > 0:
            self.data += [ line.strip() ]

    ## Helper file that writes to file
    def write_to_file(self, file_path : str) -> None:
        with open(TMP_FILE, 'w') as tmp_fd: 
            tmp_fd.write('\n'.join(self.data))

    def sort(self):
        self.data.sort()

    def __str__(self):
        return '\n'.join(self.data)


## Divide data into each of `num_nodes` lists
def divide_data(data_path : str, num_nodes : int) -> typing.List[Node_Data]:
    nodes = []
    for i in range(0, num_nodes):
        nodes += [ Node_Data() ]

    i = 0
    with open(data_path, "r") as data_fd:
        for line in data_fd:
            nodes[i % len(nodes)].add_line(line)
            i += 1

    return nodes


## For each node's work, write it to a file, run the hadoop script on it, then return results
def run_hadoop_script(nodes : typing.List[Node_Data], mapper : str) -> Node_Data:
    ret_node = Node_Data()
    for node in nodes:

        node.write_to_file(TMP_FILE)

        with open(TMP_FILE, 'r') as tmp_fd:
            cmd = []
            cmd += [ mapper ]

            map_out = subprocess.check_output(cmd,
                                              stdin=tmp_fd)
            map_str = map_out.decode('utf-8')

            for line in map_str.split('\n'):
                ret_node.add_line(line)

    return ret_node


def hadoopsim(data_path : str, mapper_path : str, reducer_path : str, num_nodes : int) -> None:

    ## Divide large data file into smaller sets of data
    mapper_nodes_work = divide_data(data_path, num_nodes)

    ## Run mapper scripts on each of the smaller data sets
    out_data_node = run_hadoop_script(mapper_nodes_work, mapper_path)

    ## Sort the output for the reducer
    out_data_node.sort()

    ## Run the one (default for hadoop) reducer file to get final result
    out_data_node = run_hadoop_script([ out_data_node ], reducer_path)

    print(out_data_node)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", help="path to data",
                        type=str, required=True)
    parser.add_argument("-m", "--mapper", help="path to mapper",
                        type=str, required=True)
    parser.add_argument("-r", "--reducer", help="path to reducer",
                        type=str, required=True)
    parser.add_argument("-n", "--nodes", help="number of mapper nodes",
                        type=int, required=True)
    args = parser.parse_args()

    hadoopsim(args.data, args.mapper, args.reducer, args.nodes)

