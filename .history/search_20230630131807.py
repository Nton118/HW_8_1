from datetime import datetime
from db.models import Author, Quote
import db.connect


def main():
    print("to search, input format <command>:<value>")
    print("available commands: name, tag, tags (multiple tags comma separated), exit")
    while True:
        command, *value = input(">>>").split(":")
        match command:
            case "name":
                name = str(value[0]).strip()

            case "tag":
                tag = str(value[0]).strip()
                quotes = Quote.objects(tags__name=tag)
                for quote in quotes:
                    print(quote.qoute)
            case "tags":
                tags_ = str(value[0]).strip().split(",")
                tags = [tag.strip() for tag in tags_]

            case "exit":
                print("good bye!")
                break

            case _:
                print("No such command. Try again")


if __name__ == "__main__":
    main()
