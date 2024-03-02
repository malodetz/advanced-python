import fileinput


def nl():
    line_number = 1
    for line in fileinput.input():
        print(f"{line_number:6}  {line.strip()}")
        line_number += 1


if __name__ == "__main__":
    nl()
