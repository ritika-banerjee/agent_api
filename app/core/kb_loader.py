import json
from functools import lru_cache

@lru_cache(maxsize=1)
def load_kb():
    with open("kb/bbq_nation_kb.json") as f:
        return json.load(f)
