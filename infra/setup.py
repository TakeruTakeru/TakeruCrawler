from venv import EnvBuilder
import sys
import os
def main():
    sys.path.append(os.getcwd())

if __name__ == "__main__":
    print(sys.path)
    main()
    print(sys.path)