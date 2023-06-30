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
                quotes = Quote.objects(
                    author=Author.objects.get(fullname__startswith=name)
                )
                for quote in quotes:
                    print(quote.quote)

            case "tag":
                tag = str(value[0]).strip()
                quotes = Quote.objects(tags__startswith=tag)
                for quote in quotes:
                    print(quote.quote)

            case "tags":
                tags_ = str(value[0]).strip().split(",")
                tags = [tag.strip() for tag in tags_]
                quotes = Quote.objects(tags__in=tags)
                for quote in quotes:
                    print(quote.quote)

            case "exit":
                print("good bye!")
                break

            case _:
                print("No such command. Try again")


if __name__ == "__main__":
    main()
