import os
import pandas as pd
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction
from ulauncher.api.shared.event import ItemEnterEvent, KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

characters = [
    "Bayonetta",
    "Bowser Jr",
    "Bowser",
    "Captain Falcon",
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
    "Pac-Man",
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
    "Chrom",
    "Ken",
    "Simon",
    "Richter",
    "Isabelle",
    "Mii Swordfighter",
    "Mii Gunner",
    "Piranha Plant",
    "Joker",
    "Hero",
    "Banjo-Kazooie",
    "Terry",
    "Byleth",
    "Min Min",
    "Steve",
    "Sephiroth",
    "Pyra & Mythra",
    "Kazuya",
    "Sora",
]

extensions_dir = f".local/share/ulauncher/extensions/framedata/"
home_dir = os.path.realpath(".")


def render_help() -> list[ExtensionResultItem]:
    return [
        ExtensionResultItem(
            icon="images/logo.png",
            name="Framedata",
            description="usage: fd character_name move_name",
            on_enter=HideWindowAction(),
        )
    ]


def render_character_framedata(data_path: str, move: str) -> list:
    # the to-be-rendered items
    items = []

    # read framedata from the csv file
    df = pd.read_csv(data_path)

    if len(move.strip()) == 0:
        df = df.head(5)

        for _, row in df.iterrows():
            items.append(
                ExtensionResultItem(
                    # icon="images/icon.png",
                    name=str(row["Move name"]),
                    description=f"F: {row['Startup'].strip()}, ADV: {row['Advantage'].strip()}, LL: {row['Landing lag'].strip()}, DMG: {row['Base damage'].strip()}%",
                    on_enter=HideWindowAction(),
                )
            )
    else:
        df = pd.read_csv(data_path, index_col='Move name')

        move_list = [m for m in list(df.index) if move.strip() in m.lower()]
        df = df.loc[move_list]

        for i, row in df.iterrows():
            items.append(
                ExtensionResultItem(
                    # icon="images/icon.png",
                    name=i,
                    description=f"F: {row['Startup'].strip()}, ADV: {row['Advantage'].strip()}, LL: {row['Landing lag'].strip()}, DMG: {row['Base damage'].strip()}%",
                    on_enter=HideWindowAction(),
                )
            )

    return items


def render_character_list(characters: list, name: str) -> list:
    # the to-be-rendered items
    items = []

    same_prefix_chars = [c for c in characters if name.title() in c]
    print(same_prefix_chars)

    # print at most 10 characters
    for c in same_prefix_chars[:10]:
        items.append(
            ExtensionResultItem(
                icon=f"images/icons/{c}.png",
                name=c,
                on_enter=SetUserQueryAction(f"fd {c}, "),
            )
        )

    return items


class DemoExtension(Extension):
    def __init__(self) -> None:
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension) -> RenderResultListAction:
        # get the character name from the inserted query
        query = event.get_argument()
        name = query.split(",")[0] or query

        try:
            move = query.split(",")[1] or ""
        except:
            move = ""

        print(name, move)

        # fetch framedata if file for selected char is found
        data_path = f"{home_dir}/{extensions_dir}/data/{name.lower()}_framedata.csv"

        # only load from disk if file exists
        if len(name.strip()) == 0:
            items = render_help()
        elif os.path.exists(data_path):
            items = render_character_framedata(data_path, move)
        else:
            items = render_character_list(characters, name)

        return RenderResultListAction(items)


if __name__ == "__main__":
    DemoExtension().run()

    # data_path = r'/home/impasse/.local/share/ulauncher/extensions/framedata/data/bayonetta_framedata.csv'
    # df = pd.read_csv(data_path, index_col='Move name')

    # move_list = list(df.index)
    # move_list = [m for m in list(df.index) if "jab" in m.lower()]

    # df = df.loc[move_list]

    # print(df)
