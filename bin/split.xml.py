#!/usr/bin/env python3

import argparse
import re
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str)
parser.add_argument('-t', '--tag',  type=str)
parser.add_argument('-n', '--num',  type=int)    # 100000 くらいがよいかも
args = parser.parse_args()

file_in = args.file
tag_pattern = args.tag
num_max = args.num

header = []
body = []
footer = []
num = 0
num_out = 0
str_header = ""
str_body   = ""

file_base = re.sub(".xml", "", file_in)

with open(file_in, "r") as f:
    for line in f:
        if re.search('<' + tag_pattern + "(\s|>)", line):
            body.append(line)

            if str_header == "":
                str_header = "".join(header)
                str_footer = "\n".join(footer) + "\n"
                
            while True:
                line = f.readline()
                body.append(line)
                
                if re.search('</' + tag_pattern + "(\s|>)", line):
                    num += 1

                    if num == num_max:
                        num_out += 1
                        file_out = file_base + '.' + '{0:03d}'.format(num_out) + '.xml'
                        # print(file_out)
                        f_out = open(file_out, 'x')

                        str_body = "".join(body)
                        f_out.write(str_header)
                        f_out.write(str_body)
                        f_out.write(str_footer)
                        f_out.close()
                        
                        body = []
                        num = 0
                        
                    break

        if str_header == "":
            header.append(line)
            
            if re.search(r"<[^\?]", line):
                tag_str = re.search(r"<[^>\s]+", line)
                each_footer = re.sub("<", "</", tag_str.group()) + ">"
                footer.insert(0, each_footer)
