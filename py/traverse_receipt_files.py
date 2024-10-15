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
    # wo_2_3.1415.pdf
    # prefix: wo_2_
    # middle: 3.1415
    # suffix: .pdf
    match = re.match(r'(\w*)_([\d.]+)(\.[^.]+)', s)
    if match:
        prefix = match.group(1)
        middle = match.group(2)
        suffix = match.group(3)
        return prefix, middle, suffix
    else:
        return None, None, None


def traverse_dir(root_path):
    total = 0.0
    for r, dirs, files in os.walk(root_path):
        for d in dirs:
            if d.startswith('.'):
                continue

            sub_dir = os.path.join(root_path, d)
            total_sum = traverse_dir(sub_dir)
            total += total_sum
            print(f"TOTAL_ROOT {total_sum} UNDER {os.path.basename(sub_dir)}")

            # total_root = 0.0
        for filename in files:
            if filename.startswith('.'):
                continue

            p, m, s = extract_parts(filename)
            if p is None or m is None or s is None:
                # print(f"NOT MATCH in DIR: {root_path}/{filename}")
                continue
            # print(f"HIT in DIR - {root_path}/{filename}\n\tprefix:{p}\n\tmiddle:{m}\n\tsuffix:{s}")
            try:
                total += float(m)
                print(f"TOTAL_ROOT {float(m)} UNDER {os.path.join(os.path.basename(r), filename)}")

            except ValueError:
                print(f"ERROR: {m}")

        return round(total, 2)

    return round(total, 2)


if __name__ == "__main__":
    path = parse_args(len(sys.argv), sys.argv)
    if path is None:
        exit(-1)

    print(f"TOTAL {traverse_dir(path)}")
    print("TASK DONE!")
    exit(0)
