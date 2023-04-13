#!/usr/bin/python3
"""module that reads from standard input and computes metrics
"""


def print_stats(size_file, sts_codes):
    """displays accumulated metrics
    """
    print("File size: {}".format(size_file))
    for key in sorted(sts_codes):
        print("{}: {}".format(key, sts_codes[key]))


if __name__ == "__main__":
    import sys

    size_file = 0
    sts_codes = {}
    correct_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    cnt = 0

    try:
        for line in sys.stdin:
            if cnt == 10:
                print_stats(size_file, sts_codes)
                cnt = 1
            else:
                cnt += 1

            line = line.split()

            try:
                size_file += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in correct_codes:
                    if sts_codes.get(line[-2], -1) == -1:
                        sts_codes[line[-2]] = 1
                    else:
                        sts_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size_file, sts_codes)

    except KeyboardInterrupt:
        print_stats(size_file, sts_codes)
        raise
