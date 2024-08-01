import argparse
from list_utils import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find differences between 2 lists')
    parser.add_argument('--list1', default='compare_list_list1.txt')
    parser.add_argument('--list2', default='compare_list_list2.txt')
    parser.add_argument('--output', default='compare_list_output.txt')

    args = parser.parse_args()

    s1 = set(read_file(args.list1))
    s2 = set(read_file(args.list2))
    s3 = s2.difference(s1)

    write_lines(s3, args.output)

