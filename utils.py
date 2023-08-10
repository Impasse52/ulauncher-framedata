import os


characters = [
    "Banjo-Kazooie",
    "Bayonetta",
    "Bowser",
    "Bowser Jr",
    "Byleth",
    "Captain Falcon",
    "Chrom",
    "Cloud",
    "Corrin",
    "Daisy",
    "Dark Pit",
    "Diddy Kong",
    "Donkey Kong",
    "Dr. Mario",
    "Duck Hunt",
    "Falco",
    "Fox",
    "Ganondorf",
    "Greninja",
    "Ice Climbers",
    "Ike",
    "Inkling",
    "Jigglypuff",
    "King Dedede",
    "Kirby",
    "Link",
    "Little Mac",
    "Lucario",
    "Lucas",
    "Lucina",
    "Luigi",
    "Mario",
    "Marth",
    "Mega Man",
    "Meta Knight",
    "Mewtwo",
    "Mii Brawler",
    "Ness",
    "Olimar",
    "Pac Man",
    "Palutena",
    "Peach",
    "Pichu",
    "Pikachu",
    "Pit",
    "Pokémon Trainer",
    "Ridley",
    "R.O.B.",
    "Robin",
    "Rosalina",
    "Roy",
    "Ryu",
    "Samus",
    "Sheik",
    "Shulk",
    "Snake",
    "Sonic",
    "Toon Link",
    "Villager",
    "Wario",
    "Wii Fit Trainer",
    "Wolf",
    "Yoshi",
    "Young Link",
    "Zelda",
    "Zero Suit Samus",
    "Game & Watch",
    "Incineroar",
    "King K. Rool",
    "Dark Samus",
    "Ken",
    "Simon",
    "Richter",
    "Isabelle",
    "Mii Swordfighter",
    "Mii Gunner",
    "Piranha Plant",
    "Joker",
    "Hero",
    "Terry",
    "Min Min",
    "Steve",
    "Sephiroth",
    "Pyra & Mythra",
    "Kazuya",
    "Sora",
]

extensions_dir = f".local/share/ulauncher/extensions/framedata/"
home_dir = os.path.realpath(".")


def pathify(name: str) -> str:
    return name.lower().replace(" ", "_").replace(".", "")
