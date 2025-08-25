from fastapi import FastAPI
import json
import os

from card import Card

def load_all_cards(data_dir="data"):
	cards = []
	for filename in os.listdir(data_dir):
		if filename.endswith(".json"):
			with open(os.path.join(data_dir, filename), "r") as f:
				js = json.loads(f.read())
				cards.extend([Card.from_dict(d) for d in js])
	return cards

cards = load_all_cards()
card_by_id = {c.id: c for c in cards}

app = FastAPI()

@app.get("/cards/{language}/{set}/{id}")
def get_card(language: str, set: str, id: str):
    card_id = set + "-" + id
    card = card_by_id.get(card_id)
    if card:
        card_name = card.name.get(language)
        if card_name:
            return {"id": card.id, "category": card.category, "name": card_name}
        else:
            return {"error": "Language not found"}, 404
    return {"error": "Card not found"}, 404
