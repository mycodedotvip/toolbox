import os
import re
import sys


def parse_args(argc, argv):
    if argc != 2 or len(argv) != argc:
        print("Usage: python %s PATH" % argv[0])
        return None
    return argv[1]


def extract_parts(s):
    # 使用正则表达式提取前缀、中间部分和后缀
    # wo_kao_3.1415.pdf
    # prefix: wo_kao_
    # middle: 3.1415
    # suffix: .pdf
    match = re.match(r'(.*_)(\w+)\.([^.]+)', s)
    if match:
        prefix = match.group(1)
        middle = match.group(2)
        suffix = match.group(3)
        return prefix, middle, suffix
    else:
        return None, None, None


if __name__ == "__main__":
    path = parse_args(len(sys.argv), sys.argv)
    if path is None:
        exit(-1)

    for root, _, files in os.walk(path):
        for filename in files:
            if filename.startswith('.'):
                continue

            p, m, s = extract_parts(filename)
            if p is None or m is None or s is None:
                print(f"NOT MATCH in DIR: {root}/{filename}")
                continue
            print(f"HIT in DIR - {root}/{filename}\n\tprefix:{p}\n\tmiddle:{m}\n\tsuffix:{s}")

    print("TASK DONE!")
    exit(0)
