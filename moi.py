import json

tallennus_data = {
    "hp": 5,
    "ase": "m9",
    "huone": "makuuhuone"
}

with open("save.json", "w") as f:
    json.dump(tallennus_data, f)

with open("save.json", "r") as f:
    luettu_data = json.load(f)

print(f"{luettu_data["hp"]}, {luettu_data["ase"]}, {luettu_data["huone"]}")

hp = 6
ase = "homo"
huone = "idk"

print(f"{hp}, {ase}, {huone}")

hp, ase, huone = luettu_data["hp"], luettu_data["ase"], luettu_data["huone"]

print(f"{hp}, {ase}, {huone}")