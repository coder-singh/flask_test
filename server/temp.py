import os


def get_last_n_offset(file, n, bsize=1):
    pos, line_count = 0, 0
    with open(file, 'rb') as f:
        f.seek(0, os.SEEK_END)
        while line_count <= n:
            if bsize > f.tell():
                return 0
            f.seek(-bsize, os.SEEK_CUR)
            line_count += f.read(bsize).count(b'\n')
            f.seek(-bsize, os.SEEK_CUR)

        while line_count > n:
            if f.read(1).count(b'\n') == 1:
                line_count -= 1

        return f.tell()


def get_lines_from_offset(file, offset):
    lines = []
    with open(file, 'r') as f:
        f.seek(offset)
        for line in f:
            lines.append(line)
    with open(file, 'rb') as f:
        f.seek(0, os.SEEK_END)
        last_pos = f.tell()
    return last_pos, lines


# last = get_last_n_offset('app.log', 0)
# print(last)
# print(get_lines_from_offset('app.log', last))
