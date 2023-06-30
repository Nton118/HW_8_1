from datetime import datetime
from db.models import Author, Quote
import db.connect


def main():
    print("to search, input format <command>:<value>")
    print("available commands: ")
    while True:
        command, value = input(">>>")


if __name__ == "__main__":
    main()
