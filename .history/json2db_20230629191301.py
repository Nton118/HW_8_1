import json
from datetime import datetime
from db.models import Author, Quote
import connect

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
        author_id = q_data.pop("author")
        quo_i.author = Author.objects.get(id=author_id)
        quo_i.quote = quote["quote"]
        quo_i.save()


def create_collections_from_json():
    with open("authors.json", "r") as authors_file:
        authors_data = json.load(authors_file)
        for author_data in authors_data:
            author = Author(**author_data)
            author.save()

    with open("quotes.json", "r") as quotes_file:
        quotes_data = json.load(quotes_file)
        for quote_data in quotes_data:
            author_id = quote_data.pop("author")
            author = Author.objects.get(id=author_id)
            quote = Quote(author=author, **quote_data)
            quote.save()
