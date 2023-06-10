import os
import json


class Style(object):

    def __init__(self, lang) -> None:
        self.style_json = None
        with open(os.path.realpath("./layouts/{}/style.json".format(lang)), "r") as f:
            self.style_json = json.load(f)
        
        self.style_def = self.style_json["style_def"]
        self.keys_style = self.style_json["keys_style"]
        self.style_by_type = self.keys_style["by_type"]
        self.style_by_keycode = self.keys_style["by_keycode"]
        self.keymap_style = self.style_json["keymap_style"]


    def get_style_by_type(self, type):
        stl = self.style_by_type[str(type)] if str(type) in self.style_by_type.keys() else None
        dstl = self.style_def[stl["style"]] if stl is not None and stl["style"] in self.style_def.keys() else None

        return dstl if dstl is not None else None
    
    def get_style_by_keycode(self, keycode):
        
        stl = self.style_by_keycode[str(keycode)] if keycode in self.style_by_keycode.keys() else None    
        dstl = self.style_def[stl["style"]] if stl is not None and stl["style"] in self.style_def.keys() else None

        return None if dstl is None else dstl
    

    def get_style_by_keycode_prop(self, keycode, property):
        stl = self.get_style_by_keycode(keycode)

        return None if stl is None else stl[property]
    

    def get_keymap_style(self):
        return self.keymap_style