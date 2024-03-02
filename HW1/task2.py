import sys


def process_file(file_name: str):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines[-10:]:
            print(line.strip())


def tail():
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            for file_name in sys.argv[1:]:
                print(f"==> {file_name} <==")
                process_file(file_name)
        else:
            process_file(sys.argv[1])
    else:
        lines = sys.stdin.readlines()
        for line in lines[-17:]:
            print(line.strip())


if __name__ == "__main__":
    tail()
