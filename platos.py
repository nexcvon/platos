
class Comment:

    def __init__(self, text):
        self.data = [text]

    def __repr__(self):
        return repr("\n".join(self.data))


class Mult:

    def __init__(self, text):
        self.data = [text]

    def __repr__(self):
        return repr("\n".join(self.data))


def loads(text):
    stack = [None] * 100
    for line in text.split("\n"):
        level = 0
        while line[:2] == "  ":
            level += 1
            line = line[2:]
        mark = line[:2]
        if mark == "# ":
            stack[level] = Comment(line[2:])
        elif mark == "$ ":
            stack[level] = Mult(line[2:])
        elif mark == "* ":
            stack[level] = [line[2:]]
        elif mark == "% ":
            stack[level] = {}
            stack[level + 1] = line[2:]
        else:
            stack[level] = line
        if type(stack[level - 1]) in [Comment, Mult]:
            stack[level - 1].data.append(stack[level])
        elif type(stack[level - 1]) is list:
            stack[level - 1].append(stack[level])
        elif type(stack[level - 2]) is dict and type(stack[level - 1]) is str:
            stack[level - 2][stack[level - 1]] = stack[level]
    print(stack[0])
    # assert len(stack) == 1
    return stack[0]


def _dump_lines(obj, lines, level, mark):
    tp = type(obj)
    prefix = "  " * level + mark
    if tp is str:
        if not ("\n" in obj or "#" in obj or "$" in obj or "*" in obj):
            lines.append(prefix + obj)
        else:
            mark = "$ "
            for line in obj.split("\n"):
                lines.append(prefix + mark + line)
                mark = "  "
    elif tp is list:
        mark = "* "
        for item in obj:
            _dump_lines(item, lines, level + 1, mark)
            mark = "  "
    elif tp is dict:
        mark = "% "
        for key, value in obj.items():
            _dump_lines(key, lines, level + 1, mark)
            mark = "  "
            _dump_lines(value, lines, level + 2, "  ")
    else:
        raise TypeError("{} is not supported".format(tp))
    return lines


def dumps(obj):
    return "\n".join(_dump_lines(obj, [], -1, ""))
