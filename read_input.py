def read_input(filename, to_num=None):
    lines = open(filename).readlines()
    if to_num is not None:
        lines = [to_num(l.strip()) for l in lines]
    return lines
