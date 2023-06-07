from .style import Style
from .keycode import Color, Key
import json

class Keymap(object):
    def __init__(self, lang) -> None:
        self.style = Style(lang)
        self.keymap_json = None
        with open("layouts/{}/keymap.json".format(lang), "r") as k:
            self.keymap_json = json.load(k)
            
        self.keycodes_json = None
        with open("layouts/{}/keycodes.json".format(lang), "r") as kj:
            js = json.load(kj)
            self.keycodes_json = js["keycodes"] 

        self.keymap = self.keymap_json["keymap"]
        self.keymap_style = self.style.get_keymap_style()
        self.margins = 0 if self.keymap_style is None else self.keymap_style["margins"]
        self.keys_height = 5 if self.keymap_style is None else self.keymap_style["keys_height"]
        self.background = Color(js=self.keymap_style["background"])

        self.keys = []
        self.keys_dict = {}
        x = 0
        y = 0
        for line in self.keymap:
            l = []
            for col in line:
                k = Key(self.style, col, self.keycodes_json[str(col)])
                k.key_style.pos_x = x
                k.key_style.pos_y = y
                x += k.key_style.width + self.margins
                l.append(k)
                self.keys_dict[col] = k
            x = 0
            y += self.margins + self.keys_height

            self.keys.append(l)


        


