import json

from db.models import Author, Quote
import db.connect


with open("authors.json", "r", encoding="utf-8") as authors:
    data = json.load(authors)
    print(data)

for author in data:
    auth_i = Author()
    auth_i.name

with open("quotes.json", "r", encoding="utf-8") as qu:
    data = json.load(qu)
    print(data)
