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

def find_card_by_id(cards, card_id):
    for card in cards:
        if card.id == card_id:
            return card
    return None  # Not found

cards = load_all_cards()
card_by_id = {c.id: c for c in cards}

app = FastAPI()

@app.get("/cards/{language}/{set}/{id}")
def get_card(language: str, set: str, id: str):
    card_id = set + "-" + id
    card = card_by_id.get(card_id)
    if card:
        return {"id": card.id, "name": card.name[language]}
    return {"error": "Card not found"}, 404