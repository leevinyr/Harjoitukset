from entity import Item
import random

random_cash_amount = random.randint(1,5)

banana = Item("Banana", 1)
gold_coin = Item("Diamond", 10)
old_necklace = Item("Old Necklace", 6)
silver_key = Item("Silver Key", 0)
headphones = Item("Headphones", 4)
guitar = Item("Guitar", 5)
dirty_microwave = Item("Dirty Microwave", 2)
rusty_bicycle = Item("Rusty Bicycle", 3)
wallet = Item("Wallet", 7)
gold_coin = Item("Gold Coin", 9)
gun = Item("Gun", 8)
coffee_mug = Item("Coffee Mug", 1)
tv_remote = Item("TV Remote", 2)
toothbrush = Item("Toothbrush", 1)
shiny_frying_pan = Item("Shiny Frying Pan", 3)
phone_charger = Item("Phone Charger", 2)
wrist_watch = Item("Steel Watch", 4)
cash = Item(f"{random_cash_amount}$ in cash", random_cash_amount)
polaroid_camera = Item("Polaroid Camera", 4)
niche_fragrance = Item("Niche Fragrance", 5)

items = [banana, gold_coin, old_necklace, silver_key, headphones, guitar,
         dirty_microwave, rusty_bicycle, wallet, gold_coin, gun, coffee_mug,
         tv_remote, toothbrush, shiny_frying_pan, phone_charger, wrist_watch,
         cash, polaroid_camera, niche_fragrance]