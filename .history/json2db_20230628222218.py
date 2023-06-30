import json
from datetime import datetime
from db.models import Author, Quote
import db.connect


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

with open("quotes.json", "r", encoding="utf-8") as qu:
    data = json.load(qu)
    print(data)
