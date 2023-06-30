from datetime import datetime
from db.models import Author, Quote
import db.connect


def search_db(text: str) -> list:
    pass


def main():
    print("to search, input format <command>:<value>")
    print("available commands: name, tag, tags (multiple tags comma separated), exit")
    while True:
        command, *value = input(">>>").split(":")
        match command:
            case "name":
                name = str(value[0]).strip()
                print(name)
            case "tag":
                tag = str(value[0]).strip()
                print(tag)
                print(type(tag))
            case "tags":
                tags = str(value[0]).strip().split(",")
                print(tags)
            case "exit":
                print("good bye!")
                break


if __name__ == "__main__":
    main()
