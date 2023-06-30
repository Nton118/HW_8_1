import json
from datetime import datetime
from db.models import Author, Quote, DBref


with open("authors.json", "r", encoding="utf-8") as authors_file:
    a_data = json.load(authors_file)
    print(a_data)

    for author in a_data:
        auth_i = Author()
        auth_i.fullname = author["fullname"]
        auth_i.born_date = datetime.strptime(author["born_date"], "%B %d, %Y")
        auth_i.born_location = author["born_location"]
        auth_i.description = author["description"]
        auth_i.save()

with open("quotes.json", "r", encoding="utf-8") as quotes_file:
    q_data = json.load(quotes_file)
    print(q_data)

    for quote in q_data:
        quo_i = Quote()
        quo_i.author = DBref(quote["author"])
        quo_i.quote = quote["quote"]
        quo_i.save()
