import os

from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.event import KeywordQueryEvent

from render import render_character_framedata, render_character_list, render_help
from utils import characters, extensions_dir, home_dir, pathify


class FramedataExtension(Extension):
    def __init__(self) -> None:
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension) -> RenderResultListAction:
        # get the character name from the inserted query and split it
        query = event.get_argument() or ""

        # split the query into name and move
        split_query = query.split(",")
        name = split_query[0].strip()

        if len(query.split(",")) > 1:
            move = split_query[1].strip()
        else:
            move = ""

        # fetch framedata if file for selected char is found
        path = f"{home_dir}/{extensions_dir}/data/{pathify(name)}_framedata.csv"

        # only load from disk if file exists
        if len(name.strip()) == 0:
            items = render_help()
        elif os.path.exists(path):
            items = render_character_framedata(path, name, move)
        else:
            items = render_character_list(characters, name)

        return RenderResultListAction(items)


if __name__ == "__main__":
    FramedataExtension().run()
