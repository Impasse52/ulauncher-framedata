from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

import pandas as pd


def build_framedata_result_items(df: pd.DataFrame, name: str) -> list:
    items = []

    # iterate on every row, each containing a move
    for move, row in df.iterrows():
        # build UFD url, to be opened on click/enter
        ufd_url = f"https://ultimateframedata.com/{name.lower()}"
        desc = f"F: {row['Startup']}, ADV: {row['Advantage']}, LL: {row['Landing lag']}, DMG: {row['Base damage']}%"

        items.append(
            ExtensionResultItem(
                icon=f"images/icons/{name}.png",
                name=move,
                description=desc,
                on_enter=OpenUrlAction(ufd_url),
            )
        )

    return items


def build_characters_result_items(chars: list, lim: int):
    items = []

    # print at most 10 characters to prevent screen overflowing
    for c in chars[:lim]:
        items.append(
            ExtensionResultItem(
                icon=f"images/icons/{c}.png",
                name=c,
                on_enter=SetUserQueryAction(f"fd {c}, "),
            )
        )

    return items


def render_help() -> list[ExtensionResultItem]:
    return [
        ExtensionResultItem(
            icon="images/logo.png",
            name="Framedata",
            description="usage: fd character_name move_name",
            on_enter=HideWindowAction(),
        )
    ]


def render_character_list(characters: list, name: str, lim: int = 10) -> list:
    # the to-be-rendered items
    items = []

    # creates a list of "similar" characters, based on common substrings
    similar_chars = [c for c in characters if name.title() in c]

    # render the items
    items = build_characters_result_items(similar_chars, lim)

    return items


def render_character_framedata(path: str, name: str, move: str, lim: int = 7) -> list:
    # the to-be-rendered items
    items = []

    # read framedata from the csv file
    df = pd.read_csv(path, index_col="Move name")

    # show a limited number of moves (a preview) when no move is queried
    if len(move.strip()) == 0:
        df = df.head(lim)
    else:
        # show a list of items containing the queried string
        move_list = [m for m in list(df.index) if move.strip() in m.lower()]

        # get a subset of the dataframe containing the filtered dataframe
        df = df.loc[move_list]

    # the list of rendered items
    items = build_framedata_result_items(df, name)

    return items
