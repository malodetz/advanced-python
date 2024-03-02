import sys
from typing import List, Tuple


def count_lines_words_chars(lines: List[str]) -> Tuple[int, int, int]:
    words = sum(len(line.split()) for line in lines)
    chars = sum(len(line) for line in lines)
    return len(lines), words, chars


def wc():
    if len(sys.argv) > 1:
        total_lines, total_words, total_chars = 0, 0, 0
        for file in sys.argv[1:]:
            with open(file, 'r') as f:
                lines_list = f.readlines()
            lines, words, chars = count_lines_words_chars(lines_list)
            print(lines, words, chars, file)
            total_lines += lines
            total_words += words
            total_chars += chars
        if len(sys.argv) > 2:
            print(total_lines, total_words, total_chars, "total")
    else:
        lines_list = sys.stdin.readlines()
        lines, words, chars = count_lines_words_chars(lines_list)
        print(lines, words, chars)


if __name__ == "__main__":
    wc()
