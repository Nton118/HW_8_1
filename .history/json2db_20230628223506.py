import json
from datetime import datetime
from db.models import Author, Quote, DBref


with open("authors.json", "r", encoding="utf-8") as authors:
    data = json.load(authors)
    print(data)

    for author in data:
        auth_i = Author()
        auth_i.fullname = author["fullname"]
        auth_i.born_date = datetime.strptime(author["born_date"], "%B %d, %Y")
        auth_i.born_location = author["born_location"]
        auth_i.description = author["description"]
        auth_i.save()

with open("quotes.json", "r", encoding="utf-8") as quotes:
    data = json.load(quotes)
    print(data)

    for quote in data:
        quo_i = Quote()
        quo_i.author = DBref(quote["author"])
        quo_i.quote = quote["quote"]
        quo_i.save()
