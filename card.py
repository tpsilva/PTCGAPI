from dataclasses import dataclass
from base_dataclass import FromDictMixin

@dataclass
class Card(FromDictMixin):
    id: str
    name: str
