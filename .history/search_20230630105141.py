from datetime import datetime
from db.models import Author, Quote
import db.connect


def main():
    print("to search, input format <command>:<value>")
    print("available commands: name, tag, tags (multiple tags comma separated), exit")
    while True:
        command, value = input(">>>").split(":")
        match command:
            case "name":
                pass
            case "tag":
                pass
            case "tags":
                pass
            case "exit":
                break


if __name__ == "__main__":
    main()
