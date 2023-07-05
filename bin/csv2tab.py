#!/usr/bin/env python3

import csv
import re
import sys

line = []

f_csv = sys.argv[1]
with open(f_csv, "r") as f:
    reader = csv.reader(f)
    line = [row for row in reader]
f.close()

f_tab = re.sub(".csv$", ".tab", f_csv)
with open(f_tab, "w") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerows(line)
f.close

