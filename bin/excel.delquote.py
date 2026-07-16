#!/usr/bin/env python3
import sys

# Excelでは、もともとデータに " " が入っていると、タブ区切りに変換した際にそのセル由来のデータをさらに " " で囲ったりするので、それを除去するためのスクリプト

def delquote(name):
    # 先頭と末尾がダブルクォートの場合は除去
    if len(name) >= 2 and name.startswith('"') and name.endswith('"'):
        name = name[1:-1]

    # "" を " に変換
    name = name.replace('""', '"')

    return name


def main():
    file_in = sys.argv[1]

    with open(file_in, "r", encoding="utf-8") as f:
        for line_in in f:
            line_in = line_in.rstrip("\r\n")

            ele = line_in.split("\t")

            output = [delquote(x) for x in ele]

            print("\t".join(output))


if __name__ == "__main__":
    main()
