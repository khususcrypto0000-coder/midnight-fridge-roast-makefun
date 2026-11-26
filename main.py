import os

ENTRY = "Spotlight on at midnight, door locked \u2014 my fridge turned my snack raid into a show I'm not allowed to watch."

assert 1 <= len(ENTRY) <= 200
assert ENTRY.strip() != ""
assert "\n" not in ENTRY

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
