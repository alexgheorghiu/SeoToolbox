def read_file(filePath):
    """Reads a file that contains a keyword per line"""
    f = open(filePath, 'r')
    lines = f.readlines();
    clear_lines = set(map(lambda l: l.strip(), lines))
    f.close()
    return clear_lines


def write_lines(lines, filePath):
    f = open(filePath, 'w')
    f.write("\n".join(lines))
    f.close()
