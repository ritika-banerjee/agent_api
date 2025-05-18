import json
import re
import string
from functools import lru_cache

def clean(text):
    return re.sub(r"\s+", "", text.translate(str.maketrans('', '', string.punctuation)).lower().strip())

@lru_cache()
def load_alias_map():
    with open("kb/alias_map.json") as f:
        return json.load(f)

def resolve_property(user_text: str) -> str | None:
    user_text = user_text.lower().strip()
    alias_map = load_alias_map()

    for prop_key, aliases in alias_map.items():
        for alias in aliases:
            if alias in user_text or clean(alias) == clean(user_text):
                return prop_key
    return None
